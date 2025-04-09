from django.db import models
from django.forms import ValidationError


from .base.base_model import BaseModel


        
class CustomerAddress(BaseModel):
    zip_code = models.CharField(max_length=8)
    street = models.CharField(max_length=255)
    complement = models.CharField(max_length=255, null=True, blank=True)
    neighborhood = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    
    
    def __str__(self):
        return f"{self.customer.name} - {self.zip_code}"