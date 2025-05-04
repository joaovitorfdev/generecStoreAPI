from django.http import HttpRequest
from ninja import Router
from api.schemas.user_schema import  UserResponse
from ninja_jwt.authentication import JWTAuth

router = Router()

@router.get("/me", response=UserResponse, auth=JWTAuth())
def get_me(request: HttpRequest):
    if not request.user.is_authenticated:
        return 404, None
    return UserResponse.model_validate(request.user)