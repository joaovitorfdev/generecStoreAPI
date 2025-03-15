from decimal import Decimal
from uuid import UUID
from pydantic import BaseModel

from api.schemas.product_schemas.stock_schema import StockBaseSchema

class ProductBaseSchema(BaseModel):
    name:str
    description:str
    category:str
    price:Decimal
    class Config:
        from_attributes = True
        
class ProductPatchSchema(BaseModel):
    name:str | None = None
    description:str | None = None
    category:str | None = None
    price:Decimal | None = None
    
class ProductResponse(ProductBaseSchema):
    id: UUID
    stocks: list[StockBaseSchema] | None = None