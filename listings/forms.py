from django import forms

#importing models
from .models import Comment, Listing, Town, Event, Industry

#importing ckeditor5
from django_ckeditor_5.widgets import CKEditor5Widget

#validation error handling
from django.core.exceptions import ValidationError


#query for the towns/wards that exist
townChoices = Town.objects.all().values_list('towns','towns')
townchoice_list = []
for item in townChoices:
    townchoice_list.append(item)

#query for the industries and categories
industryChoices = Industry.objects.all().values_list('industrys','industrys')
industrychoice_list = []
for item in industryChoices:
    industrychoice_list.append(item)

#Styles for the directory creation form
class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('name', 'owner', 'founder', 'town', 'industry', 'dir_logo', 'snippet', 'header_image', 'description')

        labels = {
            "name":  "Name of Directory",
            "founder": "Founder(s)",
            "industry": "Category",
            "dir_logo": "Logo",
            "snippet": "Summary",
            "description": "More Information",
            "header_image": "Directory Image",
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'The name of the business', 'autofocus': 'autofocus'}),
            'owner': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Owner', 'value':'', 'id':'founder', 'type':'hidden'}),
            'founder': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Founder(s)'}),
            'town': forms.Select(choices=townchoice_list, attrs={'class': 'form-control'}),
            'dir_logo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'industry': forms.Select(choices=industrychoice_list, attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'One line summary'}),
            'description': CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5", "placeholder":"Brief description of the directory"}, config_name="default"
            ),
            'header_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    #error handling
    def clean_name(self):
        name = self.cleaned_data.get('name')
        # Check if name is provided
        if not name:
            raise ValidationError("Name is required.")
        # Check minimum length
        if len(name.strip()) < 3:
            raise ValidationError("Name must be at least 3 characters long.")
        # Check uniqueness if needed (You can remove this if uniqueness is not required)
        if Listing.objects.filter(name=name).exists():
            raise ValidationError("A directory with this name already exists.")
        return name

#Styles for the directory updation form
class UpdateListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('name', 'founder', 'town', 'industry', 'dir_logo', 'snippet', 'header_image', 'description')

        labels = {
            "name":  "Name of Directory",
            "founder": "Founder(s)",
            "industry": "Category",
            "dir_logo": "Logo",
            "snippet": "Summary",
            "description": "More Information",
            "header_image": "Directory Image",
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'The name of the business', 'autofocus': 'autofocus'}),
            'founder': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Founder(s)'}),
            'town': forms.Select(choices=townchoice_list, attrs={'class': 'form-control'}),
            'industry': forms.Select(choices=industrychoice_list, attrs={'class': 'form-control'}),
            'dir_logo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'One line summary'}),
            'description': CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="default"
            ),
            'header_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


#directory comment form section
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_name', 'body')

        labels = {
            "comment_name": "Heading",
            "body": "Comment",
        }

        widgets = {
            'comment_name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


#form for the event creation/updation functionality
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_image', 'town', 'event_date', 'venue', 'fee', 'max_participants', 'event_description', 'registration_link']

        widgets = {
            'event_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'The name of the event'}),
            'town': forms.Select(choices=townchoice_list, attrs={'class': 'form-control'}),
            'venue': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'One line summary'}),
            'event_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
            'fee': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter event fee'}),
            'max_participants': forms.NumberInput(attrs={'class': 'form-control'}),
            'event_description': CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="default"
            ),
            #'event_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Brief description of the listing'}),
            'registration_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Registration link'}),
        }