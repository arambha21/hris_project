from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add custom fields here
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    department = models.ForeignKey('departments.Department', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username
