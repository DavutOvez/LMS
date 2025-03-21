from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    deleted_at = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return self.name