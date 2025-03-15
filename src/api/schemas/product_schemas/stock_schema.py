from uuid import UUID

from pydantic import BaseModel


class StockBaseSchema(BaseModel):
    size: str
    quantity: int

    class Config:
        from_attributes = True
        
class StockCreateSchema(StockBaseSchema):
    product_id: UUID

    class Config:
        from_attributes = True

class StockResponse(StockBaseSchema):
    id: UUID
    product_id: UUID  # Referência ao ID do Product

    class Config:
        from_attributes = True