from django.contrib import admin
from .models.product_models import Product,ProductImage,Stock
from .models.customer import CustomerAddress
from .models.user import User
from .models.cart import Cart,CartItem

admin.site.register(User)

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Stock)
admin.site.register(CustomerAddress)
admin.site.register(CartItem)
admin.site.register(Cart)
