from uuid import UUID
from django.http import HttpRequest
from typing import Optional
from ninja import  Router
from api.models.enums.size_enum import Sizes
from api.models.product_models import Product, Stock
from api.schemas.product_schemas.product_schema import ProductResponse, MinimumProductResponse,StockResponse
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
def list_products(request, category: Optional[str] = None):
    # Query inicial para todos os produtos, ordenados por data de criação
    products = Product.objects.order_by("-created_at")

    # Se o parâmetro 'category' for fornecido, filtra os produtos pela categoria
    if category:
        products = products.filter(category__icontains=category)  # Ajuste de acordo com o modelo de categoria

    return products

@router.get("/products/{id}", response=ProductResponse)
def get_product_by_id(request, id:UUID):
    product = Product.objects.get(id=id)
    return ProductResponse.model_validate(product)

@router.get("/products/{product_id}/stock", response=int)
def get_product_stock_by_id(request, product_id: UUID, size: Sizes):
    # Obtém a instância do produto com o UUID fornecido
    product = Product.objects.get(id=product_id)

    # Tenta obter o objeto Stock ou criar um novo se não existir
    stock, created = Stock.objects.get_or_create(product=product, size=size)

    # Retorna a quantidade de estoque (mesmo que o objeto tenha sido criado)
    return stock.quantity

