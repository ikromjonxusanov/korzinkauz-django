from django.urls import path
from .views import *
from rest_framework.views import Response

@api_view(['GET',])
def api_urls(request):
    return Response({
        "products/": "http://localhost:8000/api/products/",
        "categories/": "http://localhost:8000/api/categories/",
        "statuses/": "http://localhost:8000/api/statuses/",
        "customers/": "http://localhost:8000/api/customers/",
        "orders/": "http://localhost:8000/api/orders/",
    })
# app_name = "api"
urlpatterns = [
    path('', api_urls, name="api_urls"),
    path('products/', products),
    path('products/<int:pk>', products),
    path('categories/', categories),
    path('categories/<int:pk>', categories),
    path('statuses/', statuses),
    path('statuses/<int:pk>', statuses),
    path('customers/', customers),
    path('customer/<int:pk>', customers),
    path('orders/', orders),
    path('orders/<int:pk>', orders),
]