from .routers.public_router.api import router as public_router
from .routers.customer_router.api import router as customer_router
from .routers.customer_router.cart_routers.api import router as cart_router
from .routers.admin_router.api import router as admin_router
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_jwt.authentication import JWTAuth
from ninja_extra import NinjaExtraAPI

api = NinjaExtraAPI(
    title="GenericStore API",
    description="Backend of my personal project GenericStore",
)
 
api.register_controllers(NinjaJWTDefaultController)
api.add_router('/customer', customer_router, tags=['Customer'], auth=JWTAuth())
api.add_router('/customer', cart_router, tags=['Customer'], auth=JWTAuth())


api.add_router('/public', public_router, tags=['Products'])
api.add_router('/admin', admin_router, tags=['Admin'], auth=JWTAuth())