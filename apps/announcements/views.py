from django.views.generic import ListView
from apps.announcements.models import Announcement
from core.views import LoginRequiredMixinView
from apps.employees.models import EmployeeSetting

class AnnouncementListView(LoginRequiredMixinView, ListView):
    model = Announcement
    template_name = "announcement_list.html"
    context_object_name = "announcements"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_settings = EmployeeSetting.objects.get(actor=self.request.user)

        context["user_settings"] = user_settings
        return context