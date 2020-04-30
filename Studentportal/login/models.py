from django.db import models

# Create your models here.




class login_principle(models.Model):
    user_name_principle = models.CharField(max_length=50)
    password_principle = models.CharField(max_length=50)



class login_teacher(models.Model):
    user_name_teacher = models.CharField(max_length=50)
    password_teacher = models.CharField(max_length=50)