from rest_framework import viewsets
from main.models import Staff, Position, Shift, StaffShift, StaffAttendance
from .serializers import (
    StaffSerializer, PositionSerializer, ShiftSerializer, StaffShiftSerializer, StaffAttendanceSerializer
)

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer

class StaffShiftViewSet(viewsets.ModelViewSet):
    queryset = StaffShift.objects.all()
    serializer_class = StaffShiftSerializer

class StaffAttendanceViewSet(viewsets.ModelViewSet):
    queryset = StaffAttendance.objects.all()
    serializer_class = StaffAttendanceSerializer
