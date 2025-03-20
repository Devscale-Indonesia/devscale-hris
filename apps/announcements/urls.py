from django.urls import path
from .views import AnnouncementListView

urlpatterns = [
    path("dashboard/", AnnouncementListView.as_view(), name="announcement-list"),
]