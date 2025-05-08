from django.http import HttpRequest
from ninja import Router
from .methods import calcular_frete
from pydantic import BaseModel
from .methods import FreightItemsRequest
router = Router()

class CalculateFreightSchema(BaseModel):
    to_cep:str
    items: list[FreightItemsRequest]

@router.post("/freight")
def get_freight_amount(request:HttpRequest, model:CalculateFreightSchema):
    return calcular_frete(to_cep=model.to_cep,cart_items=model.items)
    

