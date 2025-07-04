import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    document = models.CharField(max_length=14)    
    phone = models.CharField(max_length=11)  

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        ordering = ['first_name', 'last_name']