from uuid import UUID
from django.http import HttpRequest
from ninja import Router
from api.models.product_models import Product
from api.schemas.product_schemas.product_schema import ProductResponse
from api.models.customer import  CustomerAddress
from api.models.user import User
from api.schemas.user_schema import  UserCreateRequest, UserResponse
from api.schemas.customer_schema import CustomerResponse, CustomerCreateRequest
from django.db.models import Count
from ninja_jwt.authentication import JWTAuth
from django.db import transaction
from ....models.cart import Cart,CartItem
from ....schemas.cart_schema import CartItemResponse, CartItemCreate, CartItemPatch
router = Router()

@router.post("/cart", response=CartItemResponse, auth=JWTAuth())
def add_cart_item(request: HttpRequest, model:CartItemCreate):
    if not request.user.is_authenticated:
        return 404, None
    customer_cart = Cart.objects.get(user= request.user.id)
    response = CartItem.objects.create(cart=customer_cart,**model.model_dump())
    return CartItemResponse.model_validate(response)

@router.patch("/cart/{cart_item_Id}", response={204:None}, auth=JWTAuth())
def edit_cart_item(request: HttpRequest, cart_item_Id:UUID, model:CartItemPatch):
    if not request.user.is_authenticated:
        return 404, None
    CartItem.objects.filter(id=cart_item_Id).update(**model.model_dump(exclude_unset=True))
    return 204 , None

@router.patch("/cart/{cart_item_Id}", response={204:None}, auth=JWTAuth())
def remove_cart_item(request: HttpRequest, cart_item_Id:UUID):
    if not request.user.is_authenticated:
        return 404, None
    CartItem.objects.filter(id=cart_item_Id).delete()
    return 204 , None