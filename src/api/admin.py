from django.contrib import admin
from .models.ProductModels import Product,ProductImage,Stock


admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Stock)