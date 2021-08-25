from django.contrib import admin
from .models import ProductItems, UserModel, Product, Category, Order
admin.site.register(UserModel)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductItems)
admin.site.register(Order)


# admin.site.register(Management)
# """
# C++ o'rganish va masalalar yechish

# C++ dasturlash tilini o'rganib murakkab bo'lgan masalalarni yechish va algritmik bilimni hamda logikani oshirish
# """