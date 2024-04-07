from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username