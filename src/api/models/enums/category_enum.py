from django.db import models

class Categories(models.TextChoices):
    T_SHIRTS = "t-shirts", "T-Shirts"
    HOODIES = "hoodies", "Hoodies"
    SHORTS = "shorts", "Shorts"
    ACCESSORIES = "accessories", "Accessories"
    
    @classmethod
    def choices(cls):
        return [(member.value, member.name.capitalize()) for member in cls]