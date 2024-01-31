from django.contrib import admin
from .models import Branch, Employee

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'building_number', 'street', 'area', 'city', 'country', 'manager')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email', 'phone_number', 'branch')