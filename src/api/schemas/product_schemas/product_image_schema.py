from typing import Any, Optional
from uuid import UUID
from pydantic import BaseModel, field_serializer

class ProductImageBaseSchema(BaseModel):
    is_main: bool
    
    class Config:
        from_attributes = True
    
class ProductImageCreateBaseSchema(ProductImageBaseSchema):
    is_main: bool
    product_id: UUID
    
class ProductImageResponse(BaseModel):
    is_main: bool
    image: Optional[Any] = None

    @field_serializer("image")
    def serialize_logo(self, image: Optional[Any]) -> Optional[str]:
        return image.url if image else None


    class Config:
        from_attributes = True