from django.urls import path
from .views import EventView, HomeView, DashboardView, IndustryView, ListingView, AddListingView, TownListView, UpdateListingView, DeleteListingView, TownView, LikeView, AddCommentView, event_detail, event_create, event_edit, event_delete, IndustryListView, termsView, privacyView, vihigaView, aboutView, AnalyticsView, ReportView, download_report_csv, faqsView


urlpatterns = [
    #homepage
    path('', HomeView.as_view(), name="home"),

    #dashboard
    path('dashboard/', DashboardView.as_view(), name="dashboard"),

    #directories/listings
    path('listing/<int:pk>/', ListingView.as_view(), name="listing"),
    path('add_listing/', AddListingView.as_view(), name="add_listing"),
    path('update_listing/<int:pk>/update/', UpdateListingView.as_view(), name="update_listing"),
    path('delete_listing/<int:pk>/delete/', DeleteListingView.as_view(), name="delete_listing"),

    #towns/wards
    path('town/<str:specific_town>/', TownView, name="town"),
    path('townlist/', TownListView, name="townlist"),

    #likes/comments
    path('like/<int:pk>/', LikeView, name="like_listing"),
    path('listing/<int:pk>/new_comment/', AddCommentView.as_view(), name="new_comment"),

    #events
    path('events/', EventView.as_view(), name='event_list'),
    path('events/<int:pk>/', event_detail, name='event_detail'),
    path('events/new/', event_create, name='event_create'),
    path('events/<int:pk>/edit/', event_edit, name='event_edit'),
    path('events/<int:pk>/delete/', event_delete, name='event_delete'),

    #industry/category
    path('industry/<str:specific_industry>/', IndustryView, name="industry"),
    path('industrylist/', IndustryListView, name="industrylist"),

    #footer
    path('terms-of-service/', termsView, name="terms"),
    path('privacy-policy/', privacyView, name="privacy"),
    path('vihiga/', vihigaView, name="vihiga"),
    path('about/', aboutView, name="about"),
    path('faqs/', faqsView, name="faqs"),

    #dashboard extras
    path('analytics/', AnalyticsView.as_view(), name="analytics"),
    path('report/', ReportView.as_view(), name="report"),
    path('reports/download-csv/', download_report_csv, name='download_report_csv'),
]
