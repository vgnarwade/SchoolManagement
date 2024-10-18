from django.contrib import admin
from .models import StaffNotifications, StaffLeave, StaffFeedback


admin.site.register(StaffNotifications)
admin.site.register(StaffLeave)
admin.site.register(StaffFeedback)