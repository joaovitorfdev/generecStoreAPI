from ninja import ModelSchema
from typing import Any, Optional
from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from ..models.customer import CustomerAddress

class CustomerAndressResponse(ModelSchema):
    
    class Meta:
        model = CustomerAddress
        fields = "__all__"
        
        from_attributes = True
        
class CustomerAndressCreate(ModelSchema):
    complement: str | None = None
    class Meta:
        model = CustomerAddress
        fields = "__all__"
        exclude = ["id","created_at", "disabled_at", "user"]
        from_attributes = True

    
  