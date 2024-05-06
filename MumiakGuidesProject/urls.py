from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #admin
    path('admin/', admin.site.urls),

    #listings app/directories
    path('', include("listings.urls")),

    #authentication and authorization
    path('users/', include("django.contrib.auth.urls")),
    path('users/', include("users.urls")),

    path('accounts/', include('allauth.urls')),

    #google analytics
    re_path('djga/', include('google_analytics.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#for the admin page
admin.site.site_title = "MumiakGuides"
admin.site.site_header = "MumiakGuides administration"
admin.site.index_title = "Site administration"