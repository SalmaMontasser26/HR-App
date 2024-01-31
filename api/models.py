from django.db import models
  
class Branch(models.Model):
  name = models.CharField(max_length=200)
  building_number = models.CharField(max_length=10)
  street = models.CharField(max_length=200)
  area = models.CharField(max_length=200)
  city = models.CharField(max_length=200)
  country = models.CharField(max_length=200)
  manager = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, blank=True, related_name='managed_branch')

  def __str__(self):
    return self.name

class Employee(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE, related_name='employees')
    
    def __str__(self):
      return self.name