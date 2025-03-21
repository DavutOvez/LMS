from django.db import models

# Create your models here.

GENDER = [
    ('Male','Male'),
    ('Female','Female')     
]
class Student(models.Model):
    image = models.ImageField(upload_to='stu_images/' ,null=True,blank=True)
    fullname = models.CharField(max_length=100)
    student_ID = models.CharField(max_length=10)
    gender = models.CharField(max_length=10,choices=GENDER)
    address = models.TextField()
    dob = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    school_type = models.CharField(max_length=50)
    school_name = models.CharField(max_length=100)
    school_class = models.CharField(max_length=50)
    deleted_at = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True )

    def __str__(self):
        return self.fullname 