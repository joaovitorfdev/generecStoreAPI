# api/schemas/user_schema.py
from datetime import datetime
from typing import List
from uuid import UUID

from ninja import Field, ModelSchema
from pydantic import EmailStr

from api.models import User
from api.schemas.cart_schema import CartResponse


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

class UserUpdateRequest(ModelSchema):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        ]
        from_attributes = True


class UserPatchRequest(ModelSchema):
    class Meta:
        model = User
        fields_optional = "__all__"
        exclude = ["password"]
        from_attributes = True

class UserResponse(ModelSchema):
    id: UUID
    cart: CartResponse

    class Meta:
        
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "date_joined",
        ]
        from_attributes = True
