from django.db import models

class Sizes(models.TextChoices):
    XS = "XS", "XS"
    S = "S", "S"
    M = "M", "M"
    L = "L", "L"
    XL = "XL", "XL"
    XXL = "2XL", "2XL"
    XXXL = "3XL", "3XL"
    
    @classmethod
    def choices(cls):
        return [(member.value, member.name.capitalize()) for member in cls]