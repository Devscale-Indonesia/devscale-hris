from django.views.generic import ListView
from apps.employees.models import Employee
from core.views import LoginRequiredMixinView


class EmployeeListView(LoginRequiredMixinView, ListView):
    model = Employee
    template_name = "employee_list.html"
    context_object_name = "employees"