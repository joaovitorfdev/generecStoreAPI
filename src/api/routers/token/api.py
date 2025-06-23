from ninja.errors import HttpError
from ninja import Router
from ninja_jwt.tokens import RefreshToken
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.tokens import OutstandingToken, BlacklistedToken, RefreshToken
from ninja_jwt.controller import TokenObtainPairController
from ninja_jwt.schema import TokenObtainPairInputSchema, TokenObtainPairOutputSchema, AuthUserSchema
from ninja_extra import api_controller, route
from typing import Dict, Any
from django.contrib.auth import get_user_model, authenticate
import logging
from pydantic import BaseModel
from uuid import UUID

logger = logging.getLogger(__name__)
router = Router()

class CustomTokenObtainPairOutputSchema(BaseModel):
    access: str
    refresh: str
    username: str
    user_id: UUID
    full_name: str

@api_controller("/token", tags=["token"], auth=None)
class CustomTokenObtainPairView(TokenObtainPairController):
    @route.post(
        "/pair",
        response=CustomTokenObtainPairOutputSchema,
        url_name="token_obtain_pair",
    )
    def obtain_token(self, token: TokenObtainPairInputSchema) -> Dict[str, Any]:
        try:
            logger.info(f"Attempting to obtain token for user: {token.username}")
            # Authenticate the user
            user = authenticate(username=token.username, password=token.password)
            if user is None:
                raise HttpError(401, "Invalid credentials")
            
            # Generate tokens
            refresh = RefreshToken.for_user(user)
            data = {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "username": user.username,
                "user_id": user.id,
                "full_name": f"{user.first_name} {user.last_name}".strip() or user.username
            }
            logger.info(f"Successfully obtained token for user: {token.username}")
            return data
        except Exception as e:
            logger.error(f"Error obtaining token: {str(e)}")
            raise HttpError(500, f"Error obtaining token: {str(e)}")

@router.post("/expire", auth=JWTAuth())
def logout(request, refresh_token: str):
    """
    Endpoint para logout imediato: Invalida o access token atual e o refresh token.
    """
    
    # Verifica se o header de autorização está presente
    if "HTTP_AUTHORIZATION" not in request.META:
        raise HttpError(400, "Authorization header missing.")

    auth_header = request.META["HTTP_AUTHORIZATION"]
    if not auth_header.startswith("Bearer "):
        raise HttpError(400, "Invalid authorization header format.")

    access_token = auth_header.split(" ")[1]

    try:
        # Adiciona o access token na blacklist (se configurado)
        access_outstanding_token = OutstandingToken.objects.filter(token=access_token).first()
        if access_outstanding_token:
            BlacklistedToken.objects.create(token=access_outstanding_token)

        # Invalida o refresh token
        refresh = RefreshToken(refresh_token)
        refresh.blacklist()
        
        return {"detail": "Tokens invalidated."}
    except Exception as e:
        raise HttpError(400, f"Error INvalidating  tokens: {str(e)}")