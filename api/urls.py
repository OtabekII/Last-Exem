from django.urls import path
from .views import StaffViewSet, PositionViewSet, ShiftViewSet, StaffShiftViewSet, StaffAttendanceViewSet

staff_list = StaffViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
staff_detail = StaffViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

position_list = PositionViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
position_detail = PositionViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

shift_list = ShiftViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
shift_detail = ShiftViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

staff_shift_list = StaffShiftViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
staff_shift_detail = StaffShiftViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

attendance_list = StaffAttendanceViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
attendance_detail = StaffAttendanceViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('staff/', staff_list, name='staff-list'),
    path('staff/<int:pk>/', staff_detail, name='staff-detail'),

    path('positions/', position_list, name='position-list'),
    path('positions/<int:pk>/', position_detail, name='position-detail'),

    path('shifts/', shift_list, name='shift-list'),
    path('shifts/<int:pk>/', shift_detail, name='shift-detail'),

    path('staff-shifts/', staff_shift_list, name='staffshift-list'),
    path('staff-shifts/<int:pk>/', staff_shift_detail, name='staffshift-detail'),

    path('attendance/', attendance_list, name='attendance-list'),
    path('attendance/<int:pk>/', attendance_detail, name='attendance-detail'),
]
