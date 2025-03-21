from django.db import models

# Create your models here.

class Position(models.Model):
    department = models.ForeignKey('departments.Department',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    deleted_at = models.DateTimeField(null=True,blank=True)



    def __str__(self):
        return self.name