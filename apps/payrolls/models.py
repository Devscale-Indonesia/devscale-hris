from django.db import models

from core.models import BaseModel


class Payroll(BaseModel):
    month = models.DateField()
    is_paid = models.BooleanField(default=False)
