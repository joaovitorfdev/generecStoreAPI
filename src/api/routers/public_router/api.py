from uuid import UUID
import uuid
from ninja import File, Form, Router, UploadedFile
from api.models.ProductModels import Product,ProductImage
from api.schemas.product_schemas.product_schema import ProductResponse
from api.schemas.product_schemas.product_image_schema import ProductImageCreateSchema,ProductImageResponse
from django.db.models import Count

router = Router()

@router.get("", response=list[ProductResponse])
def list_products(request):
    products = Product.objects.annotate(image_count=Count("productimage")).filter(image_count__gt=0).order_by("-created_at")
    return [ProductResponse.model_validate(p) for p in products]

@router.get("{id}", response=ProductResponse)
def get_product_by_id(request, id:UUID):
    product = Product.objects.get(id=id)
    return ProductResponse.model_validate(product)

