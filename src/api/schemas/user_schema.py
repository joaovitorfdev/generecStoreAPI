# api/schemas/user_schema.py
from typing import Optional
from uuid import UUID
from ninja import Schema, ModelSchema
from api.models import User


class UserCreateRequest(ModelSchema):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
        ]
        from_attributes = True

class UserPatchRequest(Schema):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    document: Optional[str] = None
    phone: Optional[str] = None

class UserResponse(ModelSchema):
    id: UUID
    name:str
    class Meta:
        
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "document",
            "phone",
            "date_joined",
        ]
        from_attributes = True
