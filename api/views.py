import re
from django.contrib import auth
from rest_framework.response import Response
from rest_framework.views import APIView
from api.filters import CategoryFilter, OrderFilter, ProductFilter, ProductItemsFilter, UserFilter
from .models import Category, Order, Product, ProductItems, User, UserModel
from .serializers import CategorySerializer, OrderSerializer, OrderSerializerGET, ProductItemsSerializer, ProductItemsSerializerGET, ProductSerializer, ProductSerializerGET, UserSerializer, UserRegistrationSerializer
from .responses import ResponseSuccess, ResponseFail
from .paginations import CustomPagination
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
# Create your views here.
def get_object_or_None(model, pk: int):
    try:
        return model.objects.get(id=pk)
    except:
        return None

class LoginView(APIView):

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            serializer = UserSerializer(user, many=False)
            token = Token.objects.get(user=user)
            login(request, user=user)
            print(request.user, request.auth)
            token, created = Token.objects.get_or_create(user=user)
            return ResponseSuccess({'token':token.key, 'user':serializer.data})
        else:
            return ResponseFail({
                "errors":"email or password fail"
            })
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    def delete(self, request):
        logout(request)
# {
# "email":"ikromjonkhusanov06@gmail.com",
# "password":1
# }
#
class ProductsViewSet(ViewSet):
    def __init__(self, **kwargs) -> None:
        self.MODEL = Product
        self.SERIALIZERGET = ProductSerializerGET
        self.SERIALIZER = ProductSerializer
        self.FILTER = ProductFilter
        self.FILTER_FIELDS = [
            "price_min",
            "price_max",
            "name",
            "quantities_min",
            "quantities_max",
            "create_date_start",
            "create_date_end",
            "duedate_start",
            "duedate_end",
            "code",
            "category",
        ]
        super().__init__(**kwargs)
    permission_classes = (IsAuthenticated,)
    def list(self, request):
        paginator = CustomPagination()
        paginator.page_size = 10
        query_object = self.MODEL.objects.all()
        filter = self.FILTER(request.GET, queryset=query_object)
        query_object = filter.qs
        result_page = paginator.paginate_queryset(query_object, request)
        serializer = self.SERIALIZERGET(result_page, many=True)
        return paginator.get_paginated_response(serializer.data, filter_fields=self.FILTER_FIELDS)
    def create(self, request):
        serializer = self.SERIALIZER(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseSuccess(serializer.data)
        else:
            return ResponseFail(serializer.errors)
    def retrieve(self, request, pk):
        query = get_object_or_None(self.MODEL, pk)
        if query:
            serializer = self.SERIALIZERGET(query, many=False)
            return ResponseSuccess(serializer.data)
        else:
            return ResponseFail("The ID you sent is incorrect")
    def update(self, request, pk):
        query = get_object_or_None(self.MODEL, pk)
        if query:
            serializer = self.SERIALIZER(data=request.data, instance=query)
            if serializer.is_valid():
                serializer.save()
                return ResponseSuccess(serializer.data)
            else:
                return ResponseFail("Invalid data")
        else:
            return ResponseFail("The ID you sent is incorrect")
    def destroy(self, request, pk):
        query = get_object_or_None(self.MODEL, pk)
        if query:
            query.delete()
            return ResponseSuccess("Deleted object")
        else:
            return ResponseFail("The ID you sent is incorrect")
class ProductsItemsViewSet(ViewSet):
    def __init__(self, **kwargs) -> None:
        self.MODEL = ProductItems
        self.SERIALIZERGET = ProductItemsSerializerGET
        self.SERIALIZER = ProductItemsSerializer
        self.FILTER = ProductItemsFilter
        self.FILTER_FIELDS = [
            "product",
            "quantities_min",
            "quantities_max",
            "sub_price_min",
            "sub_price_max",
            "create_date_start",
            "create_date_end",
        ]
        super().__init__(**kwargs)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        paginator = CustomPagination()
        paginator.page_size = 10
        query_object = self.MODEL.objects.all()
        filter = self.FILTER(request.GET, queryset=query_object)
        query_object = filter.qs
        result_page = paginator.paginate_queryset(query_object, request)
        serializer = self.SERIALIZERGET(result_page, many=True)
        return paginator.get_paginated_response(serializer.data, filter_fields=self.FILTER_FIELDS)
    def create(self, request):
        serializer = self.SERIALIZER(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseSuccess(serializer.data)
        else:
            return ResponseFail(serializer.errors)
    def retrieve(self, request, pk):
        query = get_object_or_None(self.MODEL, pk)
        if query:
            serializer = self.SERIALIZERGET(query, many=False)
            return ResponseSuccess(serializer.data)
        else:
            return ResponseFail("The ID you sent is incorrect")
    def update(self, request, pk):
        query = get_object_or_None(self.MODEL, pk)
        if query:
            serializer = self.SERIALIZER(data=request.data, instance=query)
            if serializer.is_valid():
                serializer.save()
                return ResponseSuccess(serializer.data)
            else:
                return ResponseFail("Invalid data")
        else:
            return ResponseFail("The ID you sent is incorrect")
    def destroy(self, request, pk):
        query = get_object_or_None(self.MODEL, pk)
        if query:
            query.delete()
            return ResponseSuccess("Deleted object")
        else:
            return ResponseFail("The ID you sent is incorrect")
class CategoriesViewSet(ViewSet):
    def __init__(self, **kwargs) -> None:
        self.MODEL = Category
        self.SERIALIZERGET = CategorySerializer
        self.SERIALIZER = CategorySerializer
        self.FILTER = CategoryFilter
        self.FILTER_FIELDS = [
            "name",
            "description"
        ]
        super().__init__(**kwargs)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        paginator = CustomPagination()
        paginator.page_size = 10
        query_object = self.MODEL.objects.all()
        filter = self.FILTER(request.GET, queryset=query_object)
        query_object = filter.qs
        result_page = paginator.paginate_queryset(query_object, request)
        serializer = self.SERIALIZERGET(result_page, many=True)
        return paginator.get_paginated_response(serializer.data, filter_fields=self.FILTER_FIELDS)
    def create(self, request):
        serializer = self.SERIALIZER(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseSuccess(serializer.data)
        else:
            return ResponseFail(serializer.errors)
    def retrieve(self, request, pk):
        query = get_object_or_None(self.MODEL, pk)
        if query:
            serializer = self.SERIALIZERGET(query, many=False)
            return ResponseSuccess(serializer.data)
        else:
            return ResponseFail("The ID you sent is incorrect")
    def update(self, request, pk):
        query = get_object_or_None(self.MODEL, pk)
        if query:
            serializer = self.SERIALIZER(data=request.data, instance=query)
            if serializer.is_valid():
                serializer.save()
                return ResponseSuccess(serializer.data)
            else:
                return ResponseFail("Invalid data")
        else:
            return ResponseFail("The ID you sent is incorrect")
    def destroy(self, request, pk):
        query = get_object_or_None(self.MODEL, pk)
        if query:
            query.delete()
            return ResponseSuccess("Deleted object")
        else:
            return ResponseFail("The ID you sent is incorrect")
class OrdersViewSet(ViewSet):
    def __init__(self, **kwargs) -> None:
        self.MODEL = Order
        self.SERIALIZERGET = OrderSerializerGET
        self.SERIALIZER = OrderSerializer
        self.FILTER = OrderFilter
        self.FILTER_FIELDS = [
            "code_min",
            "code_max",
            "sub_price_min",
            "sub_price_max",
            "orderTime_min",
            "orderTime_max",
            "date_min",
            "date_max",
            "create_date_min",
            "create_date_max",
            "status",
            "product",
        ]
        super().__init__(**kwargs)

    def list(self, request):
        paginator = CustomPagination()
        paginator.page_size = 10
        query_object = self.MODEL.objects.all()
        filter = self.FILTER(request.GET, queryset=query_object)
        query_object = filter.qs
        result_page = paginator.paginate_queryset(query_object, request)
        serializer = self.SERIALIZERGET(result_page, many=True)
        return paginator.get_paginated_response(serializer.data, filter_fields=self.FILTER_FIELDS)
    def create(self, request):
        serializer = self.SERIALIZER(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseSuccess(serializer.data)
        else:
            return ResponseFail(serializer.errors)
    def retrieve(self, request, pk):
        query = get_object_or_None(self.MODEL, pk)
        if query:
            serializer = self.SERIALIZERGET(query, many=False)
            return ResponseSuccess(serializer.data)
        else:
            return ResponseFail("The ID you sent is incorrect")
    def update(self, request, pk):
        query = get_object_or_None(self.MODEL, pk)
        if query:
            serializer = self.SERIALIZER(data=request.data, instance=query)
            if serializer.is_valid():
                serializer.save()
                return ResponseSuccess(serializer.data)
            else:
                return ResponseFail("Invalid data")
        else:
            return ResponseFail("The ID you sent is incorrect")
    def destroy(self, request, pk):
        query = get_object_or_None(self.MODEL, pk)
        if query:
            query.delete()
            return ResponseSuccess("Deleted object")
        else:
            return ResponseFail("The ID you sent is incorrect")
class UsersViewSet(ViewSet):
    def __init__(self, **kwargs) -> None:
        self.MODEL = UserModel
        self.SERIALIZERGET = UserSerializer
        self.SERIALIZER = UserSerializer
        self.FILTER = UserFilter
        self.FILTER_FIELDS = [
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "passport_code",
            "user_type",
        ]
        super().__init__(**kwargs)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        print(request.auth)
        paginator = CustomPagination()
        paginator.page_size = 10
        query_object = self.MODEL.objects.all()
        filter = self.FILTER(request.GET, queryset=query_object)
        query_object = filter.qs
        result_page = paginator.paginate_queryset(query_object, request)
        serializer = self.SERIALIZERGET(result_page, many=True)
        return paginator.get_paginated_response(serializer.data, filter_fields=self.FILTER_FIELDS)
    def create(self, request):
        serializer = self.SERIALIZER(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseSuccess(serializer.data)
        else:
            return ResponseFail(serializer.errors)
    def retrieve(self, request, pk):
        query = get_object_or_None(self.MODEL, pk)
        if query:
            serializer = self.SERIALIZERGET(query, many=False)
            return ResponseSuccess(serializer.data)
        else:
            return ResponseFail("The ID you sent is incorrect")
    def update(self, request, pk):
        query = get_object_or_None(self.MODEL, pk)
        if query:
            serializer = self.SERIALIZER(data=request.data, instance=query)
            if serializer.is_valid():
                serializer.save()
                return ResponseSuccess(serializer.data)
            else:
                return ResponseFail("Invalid data")
        else:
            return ResponseFail("The ID you sent is incorrect")
    def destroy(self, request, pk):
        query = get_object_or_None(self.MODEL, pk)
        if query:
            query.delete()
            return ResponseSuccess("Deleted object")
        else:
            return ResponseFail("The ID you sent is incorrect")
