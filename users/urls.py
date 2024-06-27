from django.urls import path
from .views import UserRegisterView, UserLogoutView, profileEditView, changePasswordView, PasswordChangeSuccess, ProfilePageView, customizedProfileEditView, CreateProfileDetailsView, user_events, user_listings
from django.contrib.auth import views as auth_views

urlpatterns = [
    #regisration
    path('register/', UserRegisterView.as_view(), name="register"),

    #logout
    path('logout_page/', UserLogoutView, name="logout_page"),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    #settings
    path('edit_profile/', profileEditView.as_view(), name="edit_profile"),

    #password
    path('password/', changePasswordView.as_view(), name="password"),
    path('password-change-success/', PasswordChangeSuccess, name="password-change-success"),

    #profile
    path('<int:pk>/profile/', ProfilePageView.as_view(), name="user_profile"),
    path('<int:pk>/edit_profile_details/', customizedProfileEditView.as_view(), name="edit_profile_details"),
    path('create_profile_details/', CreateProfileDetailsView.as_view(), name="create_profile_details"),

    #password when logged out
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"), name="password_reset_complete"),

    #listings and events for specific user
    path('user_listings/', user_listings, name='user_listings'),
    path('user_events/', user_events, name='user_events'),
]