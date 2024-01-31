from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from .utils import *

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
    'Branches List':'/branch-list/',
    'Bracnch Detail View':'/branch-detail/<str:pk>/',
    'Bracnch Create':'/branch-create/',
    'Bracnch Update':'/branch-update/<str:pk>/',
    'Bracnch Delete':'/branch-delete/<str:pk>/',
    'Employees List':'/employee-list/',
    'Employee Detail View':'/employee-detail/<str:pk>/',
    'Employee Create':'/employee-create/',
    'Employee Update':'/employee-update/<str:pk>/',
    'Employee Delete':'/employee-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def branch_list(request):
    return list_objects(request, Branch, BranchSerializer)

@api_view(['GET'])
def branch_detail(request, pk):
    return detail_object(request, Branch, BranchSerializer, pk)

@api_view(['POST'])
def branch_create(request):
    return create_object(request, Branch, BranchSerializer)

@api_view(['POST'])
def branch_update(request, pk):
    return update_object(request, Branch, BranchSerializer, pk)

@api_view(['DELETE'])
def branch_delete(request, pk):
    return delete_object(request, Branch, pk)

# Repeat similar functions for Employee model

@api_view(['GET'])
def employee_list(request):
    return list_objects(request, Employee, EmployeeSerializer)

@api_view(['GET'])
def employee_detail(request, pk):
    return detail_object(request, Employee, EmployeeSerializer, pk)

@api_view(['POST'])
def employee_create(request):
    return create_object(request, Employee, EmployeeSerializer)

@api_view(['POST'])
def employee_update(request, pk):
    return update_object(request, Employee, EmployeeSerializer, pk)

@api_view(['DELETE'])
def employee_delete(request, pk):
    return delete_object(request, Employee, pk)
