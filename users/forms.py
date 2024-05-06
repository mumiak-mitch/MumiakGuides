from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from listings.models import UserProfile

#registration form
class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'


#edit settings form
class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = None

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


#chnage password form
class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


#edit profile details form
class EditProfileDetailForm(forms.ModelForm):
        class Meta:
            model = UserProfile
            fields = ("bio", "profile_pic", "website_url", "x_url", "instagram_url", "tiktok_url", "facebook_url")
            widgets = {
                "bio" : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell your audience about yourself'}),
                #"profile_pic" : forms.TextInput(attrs={'class': 'form-control'}),
                "website_url" : forms.TextInput(attrs={'class': 'form-control'}),
                "x_url" : forms.TextInput(attrs={'class': 'form-control'}),
                "instagram_url" : forms.TextInput(attrs={'class': 'form-control'}),
                "tiktok_url" : forms.TextInput(attrs={'class': 'form-control'}),
                "facebook_url" : forms.TextInput(attrs={'class': 'form-control'}),
            }


#profile details form
class ProfileDetailsForm(forms.ModelForm):
        class Meta:
            model = UserProfile
            fields = ("bio", "profile_pic", "mobile_number", "gender", "website_url", "x_url", "instagram_url", "tiktok_url", "facebook_url")
            widgets = {
                "bio" : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell your audience about yourself'}),
                "profile_pic": forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
                "mobile_number": forms.TextInput(attrs={'class': 'form-control'}),
                "gender": forms.Select(attrs={'class': 'form-select'}),
                "website_url" : forms.TextInput(attrs={'class': 'form-control'}),
                "x_url" : forms.TextInput(attrs={'class': 'form-control'}),
                "instagram_url" : forms.TextInput(attrs={'class': 'form-control'}),
                "tiktok_url" : forms.TextInput(attrs={'class': 'form-control'}),
                "facebook_url" : forms.TextInput(attrs={'class': 'form-control'}),
            }