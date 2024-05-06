from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from django.core.validators import RegexValidator
from django_ckeditor_5.fields import CKEditor5Field


#tow/ward model
class Town(models.Model):
    towns = models.CharField(max_length=255)

    def __str__(self):
        return self.towns

#industry/category model    
class Industry(models.Model):
    industrys = models.CharField(max_length=255)

    def __str__(self):
        return self.industrys

#directory/listing model
class Listing(models.Model):
    name = models.CharField(max_length=255, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    founder = models.CharField(max_length=255, blank=True, null=True)
    header_image = models.ImageField(null=True, blank=True, upload_to="directories/")
    dir_logo = models.ImageField(null=True, blank=True, upload_to="directories/")
    description = CKEditor5Field('Description', config_name='extends', blank=True, null=True)
    #description = RichTextField(blank=True, null=True) uses ckeditor4
    date = models.DateField(auto_now_add=True)
    town = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    snippet = models.CharField(max_length=50)
    likes = models.ManyToManyField(User, related_name="listing_likes")

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.name + ' | ' + str(self.owner)

    def get_absolute_url(self):
        #return reverse('listing', args=(str(self.id)))
        return reverse('home')
    

#userprofile model
class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('female', 'Female'),
        ('male', 'Male'),
        ('other', 'Other'),
        ('prefer_not_to_say', 'Prefer not to say'),
    ]

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="profiles/")
    website_url = models.CharField(max_length=255, null=True, blank=True)
    x_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    tiktok_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True, blank=True)
    mobile_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            ),
        ],
        blank=True,
        null=True,
        help_text="Enter your mobile number in the format: '+999999999'. Up to 15 digits allowed."
    )

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')
    

#comment model 
class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    comment_name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.listing.name, self.comment_name)
    
#event model    
class Event(models.Model):
    event_name = models.CharField(max_length=255, unique=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    organizer_name = models.CharField(max_length=255, blank=True, null=True)
    event_image = models.ImageField(upload_to="events/")
    event_logo = models.ImageField(null=True, blank=True, upload_to="events/")
    event_description = CKEditor5Field('Event Description', config_name='extends', blank=True, null=True)
    event_date = models.DateField()
    town = models.ForeignKey(Town, on_delete=models.CASCADE)
    venue = models.CharField(max_length=255)
    fee = models.CharField(max_length=10)
    registration_link = models.URLField(max_length=255, null=True, blank=True)
    max_participants = models.PositiveIntegerField()

    def __str__(self):
        return self.event_name + ' | ' + str(self.organizer)

    def get_absolute_url(self):
        return reverse('event_detail', args=[str(self.id)])