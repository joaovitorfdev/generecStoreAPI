from typing import Any, Optional
from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class CustomerBaseSchema(BaseModel):
    name: str
    email: EmailStr
    document: str
    phone: str
    number: str

    class Config:
        from_attributes = True


class CustomerCreateRequest(CustomerBaseSchema):
    pass

class CustomerUpdateRequest(CustomerBaseSchema):
    pass

class CustomerPatchRequest(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    active: Optional[bool] = None

class CustomerResponse(CustomerBaseSchema):
    id: UUID
    created_at: datetime
    disabled_at: Optional[datetime] = None
    
class CustomerAndressBaseSchema(BaseModel):
    zip_code: str
    street: str
    complement: Optional[str] = None
    neighborhood: str

    class Config:
        from_attributes = True
        
class CustomerAdressCreateRequest(CustomerAndressBaseSchema):
    pass


    
  