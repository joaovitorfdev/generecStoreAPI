from datetime import datetime
from typing import List, Optional
from uuid import UUID

from ninja import Field
from pydantic import BaseModel, EmailStr

from api.schemas.customer_schema import CustomerResponse,CustomerCreateRequest
from api.schemas.group_schema import GroupResponse


class UserBaseSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr

    class Config:
        # Make sure this schema can be used with attributes from models
        from_attributes = True


# Schema for creating a new user
class UserCreateRequest(UserBaseSchema):
    password: str
    #group_id: int
   # customer_id: Optional[UUID] = None  # Optional customer ID
    
# Schema for updating user information
class UserUpdateRequest(UserBaseSchema):
    group_id: int
    customer_id: Optional[UUID] = None  # Optional customer ID
    password: Optional[str] = None

# Schema for partially updating user information (PATCH request)
class UserPatchRequest(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    group_id: Optional[int] = None
    customer_id: Optional[UUID] = None
    password: Optional[str] = None

class UserResponse(UserBaseSchema):
    id: UUID
    customer: Optional[CustomerResponse] = None    
    groups: List[GroupResponse]
    created_at: datetime = Field(..., alias="date_joined")
    
    @classmethod
    def model_validate(cls, obj, **kwargs):
        groups = [GroupResponse(id=group.id, name=group.name) for group in obj.groups.all()]
        customer = None
        if obj.customer:
            customer = CustomerResponse.model_validate(obj.customer)   
        
        return cls(**obj.__dict__, groups=groups, customer=customer, **kwargs)
    
class CreateCustomerUser(BaseModel):
    user: UserCreateRequest
    customer: CustomerCreateRequest