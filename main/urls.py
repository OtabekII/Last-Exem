from django.urls import path, include
from . import views

urlpatterns = [
    path('api/', include('api.urls')),
    path('staff/search/', views.staff_search, name='staff_search'),

    path('', views.staff_list, name='stafff_list'),  
    path('staff/create/', views.staff_create, name='staff_create'),  
    path('staff/update/<int:pk>/', views.staff_update, name='staff_update'),  
    path('staff/delete/<int:pk>/', views.staff_delete, name='staff_delete'),  

    path('positions/', views.position_list, name='position_list'),  
    path('positions/create/', views.position_create, name='position_create'),  
    path('positions/update/<int:pk>/', views.position_update, name='position_update'),  
    path('positions/delete/<int:pk>/', views.position_delete, name='position_delete'),  

    path('shifts/', views.shift_list, name='shift_list'),  
    path('shifts/create/', views.shift_create, name='shift_create'),  
    path('shifts/update/<int:pk>/', views.shift_update, name='shift_update'),  
    path('shifts/delete/<int:pk>/', views.shift_delete, name='shift_delete'),  

    path('shift-staff/', views.shiftstaff_list, name='shiftstaff_list'),  
    path('shift-staff/create/', views.shiftstaff_create, name='shiftstaff_create'),  
    path('shift-staff/update/<int:pk>/', views.shiftstaff_update, name='shiftstaff_update'),  
    path('shift-staff/delete/<int:pk>/', views.shiftstaff_delete, name='shiftstaff_delete'),  

    path('staff-attands/', views.staff_attands_list, name='staff_attands_list'),
]
