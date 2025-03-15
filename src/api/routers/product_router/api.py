import uuid
from ninja import File, Form, Router, UploadedFile
from api.models.ProductModels import Product,ProductImage
from api.schemas.product_schemas.product_schema import ProductResponse
from api.schemas.product_schemas.product_image_schema import ProductImageCreateBaseSchema,ProductImageResponse

router = Router()

@router.get("", response=list[ProductResponse])
def list_all_products(request):
    products = Product.objects.all()
    return [ProductResponse.model_validate(p) for p in products]



@router.post("/images", response={201: ProductImageResponse})
def create(
    request, 
    model: ProductImageCreateBaseSchema = Form(..., media_type="multipart/form-data"), 
    image: UploadedFile = File(None)
):
    item = ProductImage.objects.create(**model.model_dump())
    
    if image:
        file_extension = image.name.split('.')[-1]  # Obtém a extensão do arquivo
        file_name = f"{uuid.uuid4()}.{file_extension}"
        
        item.image.save(file_name, image.file)
    
    item.image_url = item.image.url if item.image else None

    return ProductImageResponse.model_validate(item)