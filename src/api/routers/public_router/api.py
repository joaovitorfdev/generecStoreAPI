from uuid import UUID
from django.http import HttpRequest
from ninja import Router
from api.models.product_models import Product
from api.schemas.product_schemas.product_schema import ProductResponse
from api.models.customer import Customer
from api.models.user import User
from api.schemas.user_schema import CreateCustomerUser, UserResponse
from api.schemas.customer_schema import CustomerResponse, CustomerCreateRequest
from django.db.models import Count
from ninja_jwt.authentication import JWTAuth

router = Router()

@router.get("/me", response=UserResponse, auth=JWTAuth())
def get_me(request: HttpRequest):
    if not request.user.is_authenticated:
        return 404, None
    return UserResponse.model_validate(request.user)

@router.post("/customers", response={201: UserResponse})
def create_customer(request: HttpRequest, model: CreateCustomerUser):
    # Cria o Customer
    customer = Customer.objects.create(**model.customer.model_dump())
    
    # Prepara os dados do User
    user_data = model.user.model_dump(exclude={"customer"})
    password = user_data.pop("password")  # Remove a senha do dicionário
    
    # Cria o User com os dados e associa o customer
    user = User.objects.create(**user_data, customer=customer, is_active=True)
    user.set_password(password)  # Criptografa a senha
    user.save()  # Salva o usuário com a senha criptografada
    
    return UserResponse.model_validate(user)

@router.get("/products", response=list[ProductResponse])
def list_products(request):
    products = Product.objects.annotate(image_count=Count("productimage")).filter(image_count__gt=0).order_by("-created_at")
    return [ProductResponse.model_validate(p) for p in products]

@router.get("/products/{id}", response=ProductResponse)
def get_product_by_id(request, id:UUID):
    product = Product.objects.get(id=id)
    return ProductResponse.model_validate(product)


