from django.http import HttpRequest
from ninja import Router


router = Router()



@router.post("/freight")
def get_freight_amount(request:HttpRequest):
    # if not request.user.is_authenticated:
    #     return 404, None
    return "oi"

