from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from listings.models import Comment, Industry, Listing, Town, Event, UserProfile
from .forms import ListingForm, UpdateListingForm, CommentForm, EventForm
from django.http import HttpResponse, HttpResponseRedirect

#homepage
class HomeView(ListView):
    model = Listing
    template_name = "listing/index.html"
    ordering = ['-date']

    def get_queryset(self):
        query = self.request.GET.get('q')

        if query:
            # If a search query is present, filter the listings based on the name
            return Listing.objects.filter(name__icontains=query)
        else:
            # If no search query, return all listings
            return Listing.objects.all()
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Industry.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
        

#dashboard
class DashboardView(ListView):
    model = Listing
    template_name = "dashboard.html"
    

#listing/directory    
class ListingView(DetailView):
    model = Listing
    template_name = "listing/listing_detail.html"

    def get_context_data(self, *args, **kwargs):
        town_menu = Town.objects.all()
        context = super(ListingView, self).get_context_data(*args, **kwargs)

        tlikes = get_object_or_404(Listing, id=self.kwargs['pk'])
        total_likes = tlikes.total_likes()

        liked = False
        if tlikes.likes.filter(id=self.request.user.id).exists(): 
            liked = True

        context["town_menu"] = town_menu
        context["total_likes"] = total_likes
        context["liked"] = liked

        return context

#creating listing/directory 
class AddListingView(CreateView):
    model = Listing
    template_name = "listing/add_listing.html"
    #fields = "__all__"
    form_class = ListingForm

    def get_context_data(self, *args, **kwargs):
        town_menu = Town.objects.all()
        context = super(AddListingView, self).get_context_data(*args, **kwargs)
        context["town_menu"] = town_menu
        return context

#updating listing/directory 
class UpdateListingView(UpdateView):
    model = Listing
    template_name = "listing/update_listing.html"
    form_class = UpdateListingForm

    def get_context_data(self, *args, **kwargs):
        town_menu = Town.objects.all()
        context = super(UpdateListingView, self).get_context_data(*args, **kwargs)
        context["town_menu"] = town_menu
        return context

#updating listing/directory 
class DeleteListingView(DeleteView):
    model = Listing
    template_name = "listing/delete_listing.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        town_menu = Town.objects.all()
        context = super(DeleteListingView, self).get_context_data(*args, **kwargs)
        context["town_menu"] = town_menu
        return context
    
#town/ward    
def TownView(request, specific_town):
    town_listings = Listing.objects.filter(town=specific_town)
    return render(request, "town/town.html", {'specific_town':specific_town.title(), 'town_listings':town_listings})

def TownListView(request):
    town_menulist = Town.objects.all()
    return render(request, "town/town_list.html", {'town_menulist':town_menulist})


#likes view
def LikeView(request, pk):
    listing = get_object_or_404(Listing, id=request.POST.get("listing_id"))
    liked = False
    
    if listing.likes.filter(id=request.user.id).exists():
        listing.likes.remove(request.user)
        liked = False
    else:
        listing.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('listing', args=[str(pk)]))


#comments view
class AddCommentView(CreateView):
    model = Comment
    template_name = "comment/new_comment.html"
    #fields = "__all__"
    form_class = CommentForm

    def get_context_data(self, *args, **kwargs):
        town_menu = Town.objects.all()
        context = super(AddCommentView, self).get_context_data(*args, **kwargs)
        context["town_menu"] = town_menu
        return context
    
    def form_valid(self, form):
        form.instance.listing_id = self.kwargs['pk']
        return super().form_valid(form)
    
    success_url = reverse_lazy('home')

#event view
class EventView(ListView):
    model = Event
    template_name = "events/event_list.html"
    context_object_name = "events"  # Add this line to specify the context variable name
    ordering = ['-id']

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Event.objects.filter(event_name__icontains=query).order_by('-id')
        else:
            # Return the queryset with default ordering
            return super().get_queryset()

    def get_context_data(self, *args, **kwargs):
        context = super(EventView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context["query"] = query  # Pass the query to the template
        return context

#event details
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

# Event creation functionality
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form, 'edit': False})

# Event edit functionality
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form, 'edit': True})

#event deletion functionality
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect('event_list')

#industry/category
def IndustryView(request, specific_industry):
    spec_industry = Listing.objects.filter(industry=specific_industry)
    return render(request, "industry/industry.html", {'specific_industry':specific_industry.title(), 'spec_industry':spec_industry})

def IndustryListView(request):
    industry_menulist = Industry.objects.all()
    return render(request, "industry/industry_list.html", {'industry_menulist':industry_menulist})


#footer
def termsView(request):
    return render(request, "footer/terms.html")

def privacyView(request):
    return render(request, "footer/privacy.html")

def vihigaView(request):
    return render(request, "footer/vihiga.html")

def aboutView(request):
    return render(request, "footer/about.html")

def faqsView(request):
    return render(request, "footer/faqs.html")


#analytics
class AnalyticsView(ListView):
    model = Listing  
    template_name = "dashboard/analytics.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        context['total_listings'] = Listing.objects.count()
        context['total_events'] = Event.objects.count()
        context['total_users'] = UserProfile.objects.count()
        context['total_towns'] = Town.objects.count()
        context['total_categories'] = Industry.objects.count()
        
        return context
    

#report
class ReportView(ListView):
    model = Listing  
    template_name = "dashboard/report.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        
        if start_date and end_date:
            # Add logic here to filter data based on start and end dates
            # Assuming ListingDate is a DateTimeField in Listing model
            context['total_directories'] = Listing.objects.filter(date__range=[start_date, end_date]).count()
            context['total_events'] = Event.objects.filter(event_date__range=[start_date, end_date]).count()
        
        return context
    
#download report
def download_report_csv(request):
    # Assuming you have the necessary data to generate the report
    # You need to replace this with your actual report generation logic
    csv_content = "Your CSV content here..."
    
    # Create the HttpResponse object with CSV content
    response = HttpResponse(csv_content, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="report.csv"'
    
    return response