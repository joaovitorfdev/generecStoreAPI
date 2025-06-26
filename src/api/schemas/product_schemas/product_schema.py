from typing import Any, List, Optional
from decimal import Decimal
from uuid import UUID

from ninja import ModelSchema
from api.models import Product 
  # adjust your import path
from api.schemas.product_schemas.stock_schema import StockBaseSchema
from api.schemas.product_schemas.product_image_schema import ProductImageResponse


class ProductBaseSchema(ModelSchema):
    class Config:
        model = Product
        model_fields = [
            "name",
            "description",
            "category",
            "price",
        ]


class ProductPatchSchema(ModelSchema):
    class Config:
        model = Product
        model_fields = [
            "name",
            "description",
            "category",
            "price",
        ]
        model_exclude = []
  


class MinimumProductResponse(ModelSchema):
    image: Any 

    class Config:
        model = Product
        model_fields = ["id", "name", "price"]
        from_attributes = True

class ProductResponse(ModelSchema):
    images_urls: List[str]  # mapeia nossa property

    class Config:
        model = Product
        model_fields = "__all__"