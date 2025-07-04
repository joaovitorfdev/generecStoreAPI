import requests
from uuid import UUID
from pydantic import BaseModel
from api.models.product_models import Product
from decouple import config

TOKEN = config("MELHORENVIO_TOKEN")
FROM_CEP = config("FROM_CEP")
BASE_URL = "https://api.melhorenvio.com.br"

class FreightItemsRequest(BaseModel):
    product_id: UUID
    quantity: int

def calcular_frete(to_cep: str, cart_items: list[FreightItemsRequest]):
    url = f"https://melhorenvio.com.br/api/v2/me/shipment/calculate"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "User-Agent": "MeuApp/1.0 (contato@exemplo.com)",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    # Mapeia os produtos com os dados do banco
    product_ids = [item.product_id for item in cart_items]
    produtos_bd = Product.objects.in_bulk(product_ids)  # retorna dict {id: produto}
    products_payload = []
    for item in cart_items:
        produto = produtos_bd.get(item.product_id)
        if not produto:
            continue  # ou lançar erro se quiser
        products_payload.append({
            "width":           int(produto.width),
            "height":          int(produto.height),
            "length":          int(produto.length),
            "weight":          float(produto.weight),
            "insurance_value": float(produto.price),
            "quantity":        item.quantity
        })
        

    body = {
        "from":     { "postal_code": FROM_CEP },
        "to":       { "postal_code": to_cep },
        "products": products_payload,
        "services": "1,2,3"
    }

    
    resp = requests.post(url, json=body, headers=headers)
    resp.raise_for_status()
    return resp.json()
