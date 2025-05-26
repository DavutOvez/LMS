from django.db import models
from subjects.models import *
import ast
from multiselectfield import MultiSelectField
from employees.models import Employee
from branches.models import Branch
from seasons.models import Season
from rooms.models import Room
from subjects.models import Subject , Level
# Create your models here.

class Group(models.Model):
    PART_OF_DAY = [
        ('Morning','Morning'),
        ('Afternoon','Afternoon'),
        ('Evening','Evening')
    ]
    DAYS = [
        ('1','Monday'),
        ('2','Tuesday'),
        ('3','Wednesday'),
        ('4','Thursday'),
        ('5','Friday'),
        ('6','Saturday'),
    ]
    LANGUAGE_CHOICES = [
    ('English', 'English'),
    ('Spanish', 'Spanish'),
    ('French', 'French'),
    ('German', 'German'),
    ('Russian', 'Russian'),
    ('Chinese', 'Chinese'),
    ('Japanese', 'Japanese'),
    ('Korean', 'Korean'),
    ('Turkish', 'Turkish'),
    ('Arabic', 'Arabic'),
    ('Hindi', 'Hindi'),
    ('Italian', 'Italian'),
    ('Portuguese', 'Portuguese'),
    ('Dutch', 'Dutch'),
    ('Swedish', 'Swedish'),
    ('Polish', 'Polish'),
    ('Ukrainian', 'Ukrainian'),
    ('Greek', 'Greek'),
    ('Hebrew', 'Hebrew'),
    ('Persian', 'Persian'),
    ('Turkmen','Turkmen'),
]
    name = models.CharField(max_length=100)
    
    level = models.ForeignKey('subjects.Level', on_delete=models.CASCADE,related_name='groups')
    season = models.ForeignKey('seasons.Season',on_delete=models.CASCADE,related_name='groups')
    branch = models.ForeignKey('branches.Branch',on_delete=models.CASCADE,related_name='groups')
    capacity = models.IntegerField()
    language = MultiSelectField(max_length=100 , choices=LANGUAGE_CHOICES)
    part_of_day = models.CharField(max_length=100, choices=PART_OF_DAY)
    week_days = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.ForeignKey('rooms.Room',on_delete=models.CASCADE,related_name='groups')
    students = models.ManyToManyField('students.Student',related_name='groups')
    teacher = models.ForeignKey('employees.Employee',on_delete=models.SET_NULL,null=True,related_name='groups')
    deleted_at = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.name
    
    def get_days(self):
        return ast.literal_eval(self.week_days)
        
   

