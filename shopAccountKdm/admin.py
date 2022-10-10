from django.contrib import admin
from shopAccountKdm.models import AccountExpenses, LabourExpenses,RateSheet
# Register your models here.
admin.site.register(AccountExpenses)
admin.site.register(LabourExpenses)
admin.site.register(RateSheet)