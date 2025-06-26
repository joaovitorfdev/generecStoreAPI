from django.db import models
from .base.base_model import BaseModel
from .enums.category_enum import Categories
from .enums.size_enum import Sizes

class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, choices=Categories.choices)
    features = models.JSONField(default=list)  # lista de strings
    specifications = models.JSONField(default=dict)
    
    width = models.IntegerField()
    height = models.IntegerField()
    length = models.IntegerField()
    weight = models.DecimalField(max_digits=10, decimal_places=1)

    original_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    @property
    def stocks(self):
        """Retorna a lista de estoques do produto com os campos exigidos pelo schema."""
        return list(self.stock.values("id", "product_id", "size", "quantity"))
    
    @property
    def images_urls(self) -> list[str]:
        """
        Retorna todas as imagens (imagem.image.url) 
        do produto, na ordem que quiser (por ex: is_main primeiro).
        """
        qs = self.images.all().order_by("-is_main", "created_at")
        return [img.image.url for img in qs]
    
    @property
    def image(self):
        first_image = self.images.order_by("-is_main")[0].image.url
        if first_image:
            return first_image
    
    def __str__(self):
        return self.name

class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
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
