# api/schemas/cart_schema.py

from typing import Any, Optional
from uuid import UUID
from ninja import ModelSchema
from ..models.cart import Cart, CartItem
from .product_schemas.product_schema import ProductResponse


class CartItemCreate(ModelSchema):
    product_id:UUID
    class Meta:
        model = CartItem
        fields =  [ "quantity","size"]
        from_attributes = True

class CartItemPatch(ModelSchema):
    quantity: Optional[int] = None
    size: Optional[str] = None

    class Meta:
        model = CartItem
        fields = ["quantity", "size"]
        from_attributes = True

class CartItemResponse(ModelSchema):
    product:ProductResponse
    class Meta:
        model = CartItem
        fields = "__all__"
        exclude = ["cart"]
        from_attributes = True

        
class CartPatchRequest(ModelSchema):
    class Meta:
        model = Cart
        fields = ["service", "to_cep"]
        from_attributes = True
        
class CartResponse(ModelSchema):
    items: list[CartItemResponse] = []
    subtotal: float
    service:int
    to_cep:str
    class Meta:
        model = Cart
        fields = ["id"]
        from_attributes = True