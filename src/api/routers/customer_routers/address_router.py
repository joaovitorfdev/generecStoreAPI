from uuid import UUID
from django.http import HttpRequest
from ninja import Router
from api.schemas.customer_schema import CustomerAndressCreate, CustomerAndressResponse
from api.models.customer import  CustomerAddress

router = Router()



@router.get("/addresses", response=list[CustomerAndressResponse])
def get_addresses(request: HttpRequest):
    if not request.user.is_authenticated:
        return 404, None
    return CustomerAddress.objects.filter(user=request.user)

@router.post("/addresses", response=CustomerAndressResponse)
def add_address(request:HttpRequest, model: CustomerAndressCreate):
    if not request.user.is_authenticated:
        return 404, None
    return CustomerAddress.objects.create(user=request.user, **model.model_dump(exclude_unset=True))

@router.delete("/addresses/{address_id}", response={204:None})
def delete_address(request:HttpRequest,address_id:UUID):
    if not request.user.is_authenticated:
        return 404, None
    CustomerAddress.objects.get(id=address_id).delete
    return 204, None