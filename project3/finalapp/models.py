from django.db import models

# Create your models here.
class UsersTable(models.Model):
    uname = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)