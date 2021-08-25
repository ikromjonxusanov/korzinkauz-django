from django.urls import path
from .views import order, orders, product, products, product_items, products_items, categories, category
urlpatterns = [
    path('p/', products),
    path('p/<int:pk>', product),
    path('p/i/', products_items),
    path('p/i/<int:pk>', product_items),
    path('c/', categories),
    path('c/<int:pk>', category),
    path('o/', orders),
    path('o/<int:pk>', order),
]