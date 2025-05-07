
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_extra import NinjaExtraAPI
from .melhor_envio.routers.freight_router.api import router as freight_rounter
api = NinjaExtraAPI(
    title="GenericStore Integrations",
    description="Integrations of my Backend GenericStore",
    urls_namespace="Integrations"
)
 
api.register_controllers(NinjaJWTDefaultController)
api.add_router('/melhorenvio', freight_rounter, tags=['Customer'])