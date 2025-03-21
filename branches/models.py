from django.db import models

# Create your models here.

class Branch(models.Model):
    name = models.CharField(max_length=80)
    head_of_branch = models.OneToOneField('employees.Employee',on_delete=models.SET_NULL,null=True)
    deleted_at = models.DateTimeField(null=True,blank=True)



    def __str__(self):
        return self.name