from uuid import UUID
from django.http import HttpRequest
from ninja import Router
from ninja_jwt.authentication import JWTAuth
from ...models.cart import Cart,CartItem
from ...schemas.cart_schema import CartResponse, CartPatchRequest, CartItemCreate,CartItemPatch
router = Router()



@router.post("items", response={204: None})
def add_cart_item(request: HttpRequest, model:CartItemCreate):
    if not request.user.is_authenticated:
        return 404, None
    customer_cart = Cart.objects.get(user= request.user.id)
    cartItem, _ = CartItem.objects.get_or_create(cart=customer_cart,**model.model_dump())
    cartItem.save()
    return 204, None

@router.patch("items/{cart_item_Id}", response={204:None})
def edit_cart_item(request: HttpRequest, cart_item_Id:UUID, model:CartItemPatch):
    if not request.user.is_authenticated:
        return 404, None
    CartItem.objects.filter(id=cart_item_Id).update(**model.model_dump(exclude_unset=True))
    return 204 , None


@router.delete("items/{cart_item_Id}", response={204:None})
def remove_cart_item(request: HttpRequest, cart_item_Id:UUID):
    if not request.user.is_authenticated:
        return 404, None
    CartItem.objects.filter(id=cart_item_Id).delete()
    return 204 , None



@router.get("", response=CartResponse, auth=JWTAuth())
def get_my_cart(request: HttpRequest):
    if not request.user.is_authenticated:
        return 404, None
    return Cart.objects.get(user=request.user)

@router.patch("", response={204:None})
def edit_cart(request: HttpRequest, model:CartPatchRequest):
    if not request.user.is_authenticated:
        return 404, None
    Cart.objects.filter(user=request.user).update(**model.model_dump(exclude_unset=True))
    return 204 , None