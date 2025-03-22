from typing import Any, Optional
from pydantic import BaseModel, EmailStr, field_serializer, field_validator
from uuid import UUID
from datetime import datetime

class CustomerBaseSchema(BaseModel):
    name: str
    email: EmailStr
    document: str
    phone: str
    zip_code: str
    street: str
    complement: Optional[str] = None
    neighborhood: str
    number: str

    class Config:
        from_attributes = True


class CustomerCreateRequest(CustomerBaseSchema):
    pass

class CustomerUpdateRequest(CustomerBaseSchema):
    city_id: int
    vehicles_id: Optional[list[UUID]] = None


class CustomerPatchRequest(BaseModel):
    city_id: Optional[int] = None
    vehicles_id: Optional[list[UUID]] = None
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    active: Optional[bool] = None

class CustomerResponse(CustomerBaseSchema):
    id: UUID
    created_at: datetime
    disabled_at: Optional[datetime] = None
    
  