import uuid
from ninja import File, Form, Router, UploadedFile
from api.schemas.product_schemas.stock_schema import StockCreateSchema, StockResponse
from api.models.product_models import Product,ProductImage, Stock
from api.schemas.product_schemas.product_schema import ProductBaseSchema, ProductResponse
from api.schemas.product_schemas.product_image_schema import ProductImageBaseSchema, ProductImageCreateSchema,ProductImageResponse
from django.db.models import Count

router = Router()

@router.post("/products", response={201: ProductBaseSchema})
def create_product(request,model: ProductResponse):
  
    item = Product.objects.create(**model.model_dump())
    return ProductBaseSchema.model_validate(item)

@router.post("/stock", response={201: StockCreateSchema})
def create_product_stock(request,model: StockCreateSchema):
    item = Stock.objects.create(**model.model_dump())
    return StockResponse.model_validate(item)

@router.post("/images")
def create_product_image(
    request, 
    model: ProductImageCreateSchema = Form(..., media_type="multipart/form-data"), 
    image: UploadedFile = File(None)
):
    item = ProductImage.objects.create(**model.model_dump())
    
    if image:
        file_extension = image.name.split('.')[-1]  # Obtém a extensão do arquivo
        file_name = f"{uuid.uuid4()}.{file_extension}"
        item.image.save(file_name, image.file)
    return 201