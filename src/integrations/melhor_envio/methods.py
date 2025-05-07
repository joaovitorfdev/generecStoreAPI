import os, requests
TOKEN = os.getenv("MELHORENVIO_TOKEN")
BASE_URL = "https://api.melhorenvio.com.br"

def calcular_frete(from_cep, to_cep, products):
    url = f"{BASE_URL}/api/v2/me/shipment/calculate"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "User-Agent": "MeuApp/1.0 (contato@exemplo.com)",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    body = {
        "from": {"postal_code": from_cep},
        "to":   {"postal_code": to_cep},
        "products": products,
    }
    resp = requests.post(url, json=body, headers=headers)
    resp.raise_for_status()
    return resp.json()
