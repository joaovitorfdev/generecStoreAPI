from django.http import HttpRequest
from ninja import Router
from api.models.user import User
from api.schemas.user_schema import UserResponse, UserPatchRequest
from ninja_jwt.authentication import JWTAuth
router = Router()

@router.get("/me", response=UserResponse, auth=JWTAuth())
def get_me(request: HttpRequest):
    user = User.objects.get(id=request.user.id)
    return user

@router.patch("/me", response={204: None}, auth=JWTAuth())
def patch_me(request: HttpRequest, model: UserPatchRequest):
    user = request.user
    data = model.dict(exclude_unset=True)

    for attr, value in data.items():
        setattr(user, attr, value)

    user.save()
    return 204

