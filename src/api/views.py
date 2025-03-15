from ninja import NinjaAPI
from .routers.product_router.api import router as product_router


api = NinjaAPI(
    title="GenericStore API",
    description="Backend of my personal project GenericStore"
)

api.add_router('/products', product_router, tags=['Products'])