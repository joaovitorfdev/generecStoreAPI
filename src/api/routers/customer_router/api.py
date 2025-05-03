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

router = Router()

@router.get("/me", response=UserResponse, auth=JWTAuth())
def get_me(request: HttpRequest):
    if not request.user.is_authenticated:
        return 404, None
    return UserResponse.model_validate(request.user)