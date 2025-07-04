from .routers.token.api import router as tokens_router, CustomTokenObtainPairView
from .routers.public_router.api import router as public_router
from .routers.customer_routers.cart_router import router as cart_router
from .routers.customer_routers.address_router import router as address_router
from .routers.admin_router.api import router as admin_router
from .routers.auth_router.api import router as auth_router

from.routers.integrations.melhorenvio.api import  router as melhorenvio_router
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_jwt.authentication import JWTAuth
from ninja_extra import NinjaExtraAPI

api = NinjaExtraAPI(
    title="GenericStore API",
    description="Backend of my personal project GenericStore",
)
api.register_controllers(CustomTokenObtainPairView)
api.add_router("/tokens", tokens_router, tags=["token"], auth=None)
api.register_controllers(NinjaJWTDefaultController)
api.add_router('/cart', cart_router, tags=['Customer'], auth=JWTAuth())
api.add_router('/customer', address_router, tags=['Customer'], auth=JWTAuth())


api.add_router('/public', public_router, tags=['Products'])
api.add_router('/auth', auth_router, tags=['Auth'])
api.add_router('/admin', admin_router, tags=['Admin'], auth=JWTAuth())

api.add_router('/melhorenvio', melhorenvio_router, tags=['Melhor Envio API'])
