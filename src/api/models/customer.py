from django.db import models
from django.forms import ValidationError


from .base.base_model import BaseModel

class Customer(BaseModel):
    name = models.CharField(max_length=255)
    document = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11, unique=True)
    zip_code = models.CharField(max_length=8)
    street = models.CharField(max_length=255)
    complement = models.CharField(max_length=255, null=True, blank=True)
    neighborhood = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
        
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
        
    class Meta:
        ordering = ['name']