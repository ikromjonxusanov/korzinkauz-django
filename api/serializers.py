from rest_framework.serializers import *
from .models import UserModel, Product, ProductItems, Category, Order

class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'email', "phone_number", "image", "passport_code", "user_type"]

class UserRegistrationSerializer(Serializer):
    email = EmailField(max_length=255)
    password = CharField(max_length=255)
    confirm = CharField(max_length=255)
    def create(self, validated_data):
        if validated_data['password'] != validated_data['confirm']:
            return {'error':'Password and confirmation are not equal'}
        user = UserModel(email=validated_data['email'])
        user.set_password(validated_data['password'])
        return user

class ProductSerializerGET(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        depth = 1

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductItemsSerializerGET(ModelSerializer):
    class Meta:
        model = ProductItems
        fields = "__all__"
        depth = 2

class ProductItemsSerializer(ModelSerializer):
    class Meta:
        model = ProductItems
        fields = "__all__"

class OrderSerializerGET(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        depth = 3

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
