from .models import Category, Order, Product, ProductItems, User
from .serializers import CategorySerializer, OrderSerializer, OrderSerializerGET, ProductItemsSerializer, ProductItemsSerializerGET, ProductSerializer, ProductSerializerGET, UserSerializer, UserRegistrationSerializer
from .responses import ResponseSuccess, ResponseFail
from .paginations import CustomPagination
from rest_framework.viewsets import ViewSet

# Create your views here.
def get_object_or_None(model, pk: int):
    try:
        return model.objects.get(id=pk)
    except:
        return None

class ProductsViewSet(ViewSet):
    def __init__(self, **kwargs) -> None:
        self.MODEL = Product
        self.SERIALIZERGET = ProductSerializerGET
        self.SERIALIZER = ProductSerializer
        super().__init__(**kwargs)

    def list(self, request):
        paginator = CustomPagination()
        paginator.page_size = 10
        query_object = self.MODEL.objects.all()
        result_page = paginator.paginate_queryset(query_object, request)
        serializer = self.SERIALIZERGET(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
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
        super().__init__(**kwargs)

    def list(self, request):
        paginator = CustomPagination()
        paginator.page_size = 10
        query_object = self.MODEL.objects.all()
        result_page = paginator.paginate_queryset(query_object, request)
        serializer = self.SERIALIZERGET(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
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
        super().__init__(**kwargs)

    def list(self, request):
        paginator = CustomPagination()
        paginator.page_size = 10
        query_object = self.MODEL.objects.all()
        result_page = paginator.paginate_queryset(query_object, request)
        serializer = self.SERIALIZERGET(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
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
        super().__init__(**kwargs)

    def list(self, request):
        paginator = CustomPagination()
        paginator.page_size = 10
        query_object = self.MODEL.objects.all()
        result_page = paginator.paginate_queryset(query_object, request)
        serializer = self.SERIALIZERGET(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
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
