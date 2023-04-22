from django.contrib import admin
from .models import TimeSchedule, TimeSlot

# Register your models here.
admin.register(TimeSlot)
admin.register(TimeSchedule)
