from django.contrib import admin
from .models import Staff, Position, Shift, StaffShift, StaffAttendance

# Modellarni oddiy ro'yxatdan o'tkazish
admin.site.register(Staff)
admin.site.register(Position)
admin.site.register(Shift)
admin.site.register(StaffShift)
admin.site.register(StaffAttendance)
