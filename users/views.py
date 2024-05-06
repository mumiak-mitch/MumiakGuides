from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from listings.models import UserProfile, Listing, Event
from .forms import RegisterForm, EditProfileForm, ChangePasswordForm, ProfileDetailsForm, EditProfileDetailForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView, CreateView
from django.contrib.auth.decorators import login_required

# user registration view
class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')

def UserLogoutView(request):
    return render(request, "registration/logout.html")

#settings view
class profileEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "profile/edit_settings.html"
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

#password    
class changePasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name="registration/change-password.html"
    success_url = reverse_lazy('password-change-success')

def PasswordChangeSuccess(request):
    return render(request, "registration/pass-change-success.html")


class ProfilePageView(DetailView):
    model = UserProfile
    template_name = "profile/user_profile.html"

    def get_context_data(self, *args, **kwargs):
        #users = UserProfile.objects.all()
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context
    

#profile views
class customizedProfileEditView(generic.UpdateView):
    model = UserProfile
    template_name = "profile/edit_profile_details.html"
    form_class = EditProfileDetailForm
    success_url = reverse_lazy('home')


class CreateProfileDetailsView(CreateView):
    model = UserProfile
    template_name = "profile/create_details_view.html"
    form_class = ProfileDetailsForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

#specific user directory and event views
@login_required
def user_listings(request):
    listings = Listing.objects.filter(owner=request.user)
    return render(request, 'user/user_listings.html', {'listings': listings})

@login_required
def user_events(request):
    events = Event.objects.filter(organizer=request.user)
    return render(request, 'user/user_events.html', {'events': events})