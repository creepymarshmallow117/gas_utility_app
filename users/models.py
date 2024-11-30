from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    panNumber = models.CharField(max_length=10, unique=True, blank=True, null=True)
    is_support_staff = models.BooleanField(default=False)

