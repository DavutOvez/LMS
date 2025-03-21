from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100)
    deleted_at = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.name
    
class Level(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,related_name='levels')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    deleted_at = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return self.name