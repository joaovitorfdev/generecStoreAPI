from django.contrib import admin
from .models.product_models import Product,ProductImage,Stock
from .models.customer import Customer
from .models.user import User


admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Stock)
admin.site.register(Customer)
admin.site.register(User)