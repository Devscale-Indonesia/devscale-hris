from django.urls import path
from .views import PayrollListView

urlpatterns = [
    path("payroll/", PayrollListView.as_view(), name="payroll-list"),
]