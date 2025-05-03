from django.db import models
from .base.base_model import BaseModel
from .user import User
from .product_models import Product  
from .enums.size_enum import Sizes

class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts")
    is_active = models.BooleanField(default=True)  # permite ter histórico de pedidos

    def __str__(self):
        return f"Carrinho #{self.id} – {self.user.username}"


class CartItem(BaseModel):
  

    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="items"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=3, choices=Sizes.choices, default="M")

    class Meta:
        unique_together = ("cart", "product", "size")

    # def clean(self):
    #     if self.quantity < 1:
    #         raise ValidationError("Quantidade mínima é 1")

    @property
    def subtotal(self):
        return self.quantity * self.product.price  # presumo atributo price em Product

    def __str__(self):
        return f"{self.quantity}x {self.product.name} ({self.size()})"
