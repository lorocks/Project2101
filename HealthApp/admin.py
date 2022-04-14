from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserType)
admin.site.register(Patients)
admin.site.register(Doctors)
admin.site.register(DailyData)
admin.site.register(SecondlyData)
admin.site.register(WeeklyData)
admin.site.register(testingAPI)
admin.site.register(PatientImage)
admin.site.register(FirebaseData)
admin.site.register(Alert)
admin.site.register(IRCheck)
admin.site.register(Conditions)