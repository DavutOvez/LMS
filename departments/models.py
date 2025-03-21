from django.db import models
from employees.models import Employee
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=80)
    head_of_dep = models.OneToOneField(Employee,on_delete=models.SET_NULL,null=True ,related_name='head_department')
    deleted_at = models.DateTimeField(null=True,blank=True)


    def __str__(self):
        return self.name