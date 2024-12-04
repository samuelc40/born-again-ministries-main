from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True, null=False)
    username = models.CharField(max_length=100)
    # bio = models.CharField(max_length=100, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username
    
class Messages(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Notices(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, blank=False, null=False)
    # date = models.DateField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    # short_desc = models.TextField()
    # time = models.CharField(max_length=40, blank=True, null=True)
    desc = models.TextField()
    varify = models.BooleanField(default=False)

    def __str__(self):
        return self.title

