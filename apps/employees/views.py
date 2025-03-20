from django.views.generic import ListView
from apps.employees.models import Employee
from core.views import LoginRequiredMixinView
from apps.employees.models import EmployeeSetting

class EmployeeListView(LoginRequiredMixinView, ListView):
    model = Employee
    template_name = "employee_list.html"
    context_object_name = "employees"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_settings = EmployeeSetting.objects.get(actor=self.request.user)

        context["user_settings"] = user_settings
        return context