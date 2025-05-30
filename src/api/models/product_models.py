from django.db import models
from .base.base_model import BaseModel
from .enums.category_enum import Categories
from .enums.size_enum import Sizes

class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, choices=Categories.choices)
    
    width = models.IntegerField()
    height = models.IntegerField()
    length = models.IntegerField()
    
    weight = models.DecimalField(max_digits=10, decimal_places=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    @property
    def stocks(self):
        """Retorna a lista de estoques do produto com os campos exigidos pelo schema."""
        return list(self.stock.values("id", "product_id", "size", "quantity"))
    
    @property
    def images(self):
        return self.productimage_set.order_by("-is_main").all()
    
    
    def __str__(self):
        return self.name

class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/", blank=True)
    is_main = models.BooleanField(default=False)  

    def __str__(self):
        return f"{self.product.name} - {'Main' if self.is_main else 'Extra'}"
    
class Stock(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="stock")
    size = models.CharField(max_length=10, choices=Sizes.choices)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - {self.size}: {self.quantity}"
