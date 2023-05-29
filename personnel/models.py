from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=32)
    user_id = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Personnel(models.Model):
    first_name= models.CharField(max_length=32)
    last_name= models.CharField(max_length=32)
    GENDER=(
        ('Female', 'F'),
        ('Male', 'M'),
        ('Prefer not to say', 'N'),
    )
    gender =  models.CharField(max_length=1 , choices=GENDER, default='N')
    TITLE=(
        ('S', 'Senior'),
        ('M', 'Med-Senior'),
        ('J', 'Junior'),
    )
    title =  models.CharField(max_length=1 , choices=TITLE, default='J')
    salary= models.IntegerField()
    started = models.DateField()
    department_id = models.ForeignKey(Department, on_delete=models.SET_NULL , null=True)
    user_id = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"


