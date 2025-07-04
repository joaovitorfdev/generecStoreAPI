from decimal import Decimal
import uuid
from django.db import models

from api.routers.integrations.melhorenvio.methods import FreightItemsRequest, calcular_frete
from .base.base_model import BaseModel
from .user import User
from .product_models import Product  
from .enums.size_enum import Sizes

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cart", db_column="user_id")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    to_cep = models.CharField(max_length=8, blank=True, null=True)
    service = models.IntegerField(default=0)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True, default=None)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True, default=None)
    @property
    def total(self) -> Decimal:
        product_total = sum(item.subtotal for item in self.items.all())
        self.subtotal = product_total

        if not self.to_cep or self.service == 0 or product_total == 0:
            self.shipping_cost = None
            return product_total

        freight_requests = [
            FreightItemsRequest(
                product_id=item.product.id,
                quantity=item.quantity
            )
            for item in self.items.all()
        ]

        services = calcular_frete(to_cep=self.to_cep, cart_items=freight_requests)
        selected = next((s for s in services if s.get("id") == self.service), None)

        if not selected or not selected.get("price"):
            self.service = 0
            self.save(update_fields=["service"])
            return product_total

        price_str = selected["price"]
        shipping_cost = Decimal(price_str.replace(",", "."))
        self.shipping_cost = shipping_cost
        return product_total + shipping_cost
    
    
    def __str__(self):
        return f"Carrinho #{self.id} – {self.user.username}"

class CartItem(BaseModel):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="items", db_column="cart_id"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, db_column="product_id"
    )
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=3, choices=Sizes.choices, default="M")
    
    class Meta:
        ordering = ["size"]
        unique_together = ("cart", "product", "size")
        

    # def clean(self):
    #     if self.quantity < 1:
    #         raise ValidationError("Quantidade mínima é 1")

    @property
    def subtotal(self):
        return self.quantity * self.product.price  # presumo atributo price em Product
    
   

    def __str__(self):
        return f"{self.quantity}x {self.product.name} ({self.size})"
