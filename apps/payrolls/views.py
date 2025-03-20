from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from apps.payrolls.models import Payroll
from apps.employees.models import Employee, EmployeeSetting
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
        user_settings = EmployeeSetting.objects.get(actor=self.request.user)

        context['employee'] = employee
        context['user_settings'] = user_settings

        return context

class PayrollProcessView(LoginRequiredMixinView, View):
    def get(self, request):
        user_settings = EmployeeSetting.objects.get(actor=request.user)
        return render(request, 'payroll_process.html', {'user_settings': user_settings})

    def post(self, request):
        action = request.POST.get('action')

        if action == 'process':
            print("Processing payroll!!!")

        return redirect('payroll-process')