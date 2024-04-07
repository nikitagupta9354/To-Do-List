from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    task_name=models.CharField(max_length=100)
    description=models.TextField()
    is_completed=models.CharField(max_length=10,default='Pending')
    date=models.DateField(default=date.today)

