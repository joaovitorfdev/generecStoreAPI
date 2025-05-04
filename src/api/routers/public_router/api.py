from uuid import UUID
from django.http import HttpRequest
from ninja import Router
from api.models.product_models import Product
from api.schemas.product_schemas.product_schema import ProductResponse
from api.models.customer import  CustomerAddress
from api.models.user import User
from api.schemas.user_schema import  UserCreateRequest, UserResponse
from django.db.models import Count
from ninja_jwt.authentication import JWTAuth
from django.db import transaction

router = Router()

@router.post("/customers", response={201: UserResponse})
@transaction.atomic
def create_customer(request: HttpRequest, model: UserCreateRequest):
    user = User.objects.create(**model.model_dump(), is_active=True)
    user.set_password(model.password)
    user.save()
    
    return UserResponse.model_validate(user)

@router.get("/products", response=list[ProductResponse])
def list_products(request):
    products = Product.objects.annotate(image_count=Count("productimage")).filter(image_count__gt=0).order_by("-created_at")
    return [ProductResponse.model_validate(p) for p in products]

@router.get("/products/{id}", response=ProductResponse)
def get_product_by_id(request, id:UUID):
    product = Product.objects.get(id=id)
    return ProductResponse.model_validate(product)


