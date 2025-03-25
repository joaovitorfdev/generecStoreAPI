import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from api.models.customer import Customer

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
        
    class Meta:
        ordering = ['first_name', 'last_name']