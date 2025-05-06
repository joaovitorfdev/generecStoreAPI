from uuid import UUID
from django.http import HttpRequest
from ninja import Router
from ninja_jwt.authentication import JWTAuth
from ...models.cart import Cart,CartItem
from ...schemas.cart_schema import CartItemResponse, CartItemCreate, CartItemPatch
router = Router()

@router.post("/cart", response=CartItemResponse)
def add_cart_item(request: HttpRequest, model:CartItemCreate):
    if not request.user.is_authenticated:
        return 404, None
    customer_cart = Cart.objects.get(user= request.user.id)
    response = CartItem.objects.create(cart=customer_cart,**model.model_dump())
    return CartItemResponse.model_validate(response)

@router.patch("/cart/{cart_item_Id}", response={204:None})
def edit_cart_item(request: HttpRequest, cart_item_Id:UUID, model:CartItemPatch):
    if not request.user.is_authenticated:
        return 404, None
    CartItem.objects.filter(id=cart_item_Id).update(**model.model_dump(exclude_unset=True))
    return 204 , None

@router.delete("/cart/{cart_item_Id}", response={204:None})
def remove_cart_item(request: HttpRequest, cart_item_Id:UUID):
    if not request.user.is_authenticated:
        return 404, None
    CartItem.objects.filter(id=cart_item_Id).delete()
    return 204 , None