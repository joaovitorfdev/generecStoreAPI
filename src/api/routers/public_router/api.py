from uuid import UUID
from django.http import HttpRequest
from ninja import Router
from api.models.product_models import Product
from api.schemas.product_schemas.product_schema import ProductResponse, MinimumProductResponse
from api.models.cart import  Cart
from api.models.user import User
from api.schemas.user_schema import  UserCreateRequest, UserResponse
from django.db import transaction

router = Router()

@router.post("/register", response={201: UserResponse})
@transaction.atomic
def create_user(request: HttpRequest, model: UserCreateRequest):
    user = User(
        username=model.email,
        email=model.email,
        first_name=model.first_name,
        last_name=model.last_name,
    )
    user.set_password(model.password)
    user.save()

    Cart.objects.create(user=user)

    return UserResponse.model_validate(user)

@router.get("/products", response=list[MinimumProductResponse])
def list_products(request):
    products = Product.objects.order_by("-created_at")
    return products

@router.get("/products/{id}", response=ProductResponse)
def get_product_by_id(request, id:UUID):
    product = Product.objects.get(id=id)
    return ProductResponse.model_validate(product)


