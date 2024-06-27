from django.contrib import admin

#models imported
from .models import Listing, Town, UserProfile, Comment, Industry

# Register your models here.
admin.site.register(Listing)
admin.site.register(Town)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Industry)