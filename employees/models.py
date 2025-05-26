from django.db import models
from django.contrib.auth.models import User



# Create your models here.

GENDER = [
    ('Male','Male'),
    ('Female','Female')
]
EMP_TYPE =[ 
    ('Full-Time','Full-Time'),
    ('Part-Time','Part-Time'),
    ('Contract','Contract'),
    ('Intern','Intern')
]
class Employee(models.Model):
    image = models.ImageField(upload_to='emp_images/' , null=True,blank=True)
    fullname = models.CharField(max_length=100)
    username = models.OneToOneField(User ,on_delete=models.SET_NULL,null=True,blank=True )
    ID_num = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GENDER)
    address = models.CharField(max_length=100)
    dob = models.DateField()
    department = models.ForeignKey('departments.Department', on_delete=models.SET_NULL,null=True,blank=True,related_name='employees')
    position = models.ForeignKey('positions.Position', on_delete=models.SET_NULL,null=True,blank=True,related_name='employees')
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    emp_type = models.CharField(max_length=100 ,choices=EMP_TYPE )
    grad_uni = models.CharField(max_length=100,null=True,blank=True)
    grad_major = models.CharField(max_length=100,null=True,blank=True)
    grad_year = models.DateField(null=True,blank=True)
    deleted_at = models.DateTimeField(null=True,blank=True)


    def __str__(self):
        return self.fullname