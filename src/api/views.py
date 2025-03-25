from .routers.public_router.api import router as public_router
from .routers.admin_router.api import router as admin_router
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_jwt.authentication import JWTAuth
from ninja_extra import NinjaExtraAPI

api = NinjaExtraAPI(
    title="GenericStore API",
    description="Backend of my personal project GenericStore",
)
 
api.register_controllers(NinjaJWTDefaultController)
api.add_router('/public', public_router, tags=['Products'])
api.add_router('/admin', admin_router, tags=['Admin'], auth=JWTAuth())