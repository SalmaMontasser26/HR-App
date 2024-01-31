from django.urls import path
from .views import *

urlpatterns = [
	path('', apiOverview, name="api-overview"),
	
    path('branch-list/', branch_list, name="branch-list"),
    path('branch-detail/<str:pk>/', branch_detail, name="branch-detail"),
    path('branch-create/', branch_create, name="branch-create"),
    path('branch-update/<str:pk>/', branch_update, name="branch-update"),
    path('branch-delete/<str:pk>/', branch_delete, name="branch-delete"),
    
    path('employee-list/', employee_list, name="employee-list"),
    path('employee-detail/<str:pk>/', employee_detail, name="employee-detail"),
    path('employee-create/', employee_create, name="employee-create"),
    path('employee-update/<str:pk>/', employee_update, name="employee-update"),
    path('employee-delete/<str:pk>/', employee_delete, name="employee-delete"),
]