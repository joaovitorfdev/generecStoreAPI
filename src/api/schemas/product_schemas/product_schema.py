from decimal import Decimal
from uuid import UUID
from pydantic import BaseModel

class ProductBaseSchema(BaseModel):
    name:str
    description:str
    category:str
    price:Decimal

class ProductPatchSchema(BaseModel):
    name:str | None = None
    description:str | None = None
    category:str | None = None
    price:Decimal | None = None
    
class ProductResponse(ProductBaseSchema):
    id:UUID