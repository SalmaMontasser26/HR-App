from rest_framework import serializers
from .models import *

class BranchSerializer(serializers.ModelSerializer):
	class Meta:
		model = Branch
		fields ='__all__'
		
class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields ='__all__'