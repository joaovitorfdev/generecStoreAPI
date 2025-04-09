import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    document = models.CharField(max_length=14, null=True,  blank=True)
        
    class Meta:
        ordering = ['first_name', 'last_name']