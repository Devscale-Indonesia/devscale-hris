from django.views.generic import ListView
from apps.announcements.models import Announcement
from core.views import LoginRequiredMixinView

class AnnouncementListView(LoginRequiredMixinView, ListView):
    model = Announcement
    template_name = "announcement_list.html"
    context_object_name = "announcements"