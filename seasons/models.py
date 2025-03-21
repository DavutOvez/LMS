from django.db import models

SEASON_STATUS = [
    ('Upcoming','Upcoming'),
    ('Ongoing','Ongoing'),
    ('Completed','Completed'),
    ('Archived','Archived')
]
# Create your models here.
class Season(models.Model):



    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True,blank=True)

    
    def __str__(self):        
        return self.name