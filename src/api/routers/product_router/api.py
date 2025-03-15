from ninja import Router
from api.models.ProductModels import Product
from api.schemas.product_schemas.product_schema import ProductResponse

router = Router()

@router.get("", response=list[ProductResponse])
def list_all_products(request):
    products = Product.objects.all()
    return [ProductResponse.model_validate(p) for p in products]