from typing import Any, Optional
from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class CustomerBaseSchema(BaseModel):
    document: str
    class Config:
        from_attributes = True


class CustomerCreateRequest(CustomerBaseSchema):
    pass

class CustomerUpdateRequest(CustomerBaseSchema):
    pass

class CustomerPatchRequest(BaseModel):
    pass 

class CustomerResponse(CustomerBaseSchema):
    id: UUID
    created_at: datetime
    disabled_at: Optional[datetime] = None
    
class CustomerAndressBaseSchema(BaseModel):
    zip_code: str
    street: str
    complement: Optional[str] = None
    neighborhood: str
    number: str

    class Config:
        from_attributes = True
        
class CustomerAdressCreateRequest(CustomerAndressBaseSchema):
    pass


    
  