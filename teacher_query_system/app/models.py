from django.db import models

class Teacher(models.Model):
    department = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='spider//utils//教师头像//')

