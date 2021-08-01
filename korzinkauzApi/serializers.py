from rest_framework.serializers import *
from products.models import *

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ProductGetFkObjectSerializer(ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = "__all__"


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class CustomerGetFkObjectSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = "__all__"

class StatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class OrderGetFkObjectSerializer(ModelSerializer):
    status = StatusSerializer()
    customer = CustomerGetFkObjectSerializer()
    products = ProductGetFkObjectSerializer()
    class Meta:
        model = Order
        fields = "__all__"



