from django.views.generic import ListView
from apps.payrolls.models import Payroll
from apps.employees.models import Employee
from core.views import LoginRequiredMixinView


class PayrollListView(LoginRequiredMixinView, ListView):
    model = Payroll
    template_name = "payroll_list.html"
    context_object_name = "payrolls"

    def get_queryset(self):
        return Payroll.objects.filter(actor=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        employee = Employee.objects.filter(actor=self.request.user).first()
        print(employee)
        context['employee'] = employee

        return context