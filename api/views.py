from .models import Category, Order, Product, ProductItems, User
from .serializers import CategorySerializer, OrderSerializer, OrderSerializerGET, ProductItemsSerializer, ProductItemsSerializerGET, ProductSerializer, ProductSerializerGET, UserSerializer, UserRegistrationSerializer
from .responses import ResponseSuccess, ResponseFail
from rest_framework.decorators import api_view
# Create your views here.
from time import sleep as s
def get_object_or_None(model, pk: int):
    try:
        return model.objects.get(id=pk)
    except:
        return None

@api_view(['GET', "POST"])
def products(request):
    if request.method == "GET":
        s(1)
        query = Product.objects.all()
        serializer = ProductSerializerGET(query, many=True)
        return ResponseSuccess(serializer.data)
    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseSuccess(serializer.data)

@api_view(['GET', "PUT", "DELETE"])
def product(request, pk):

    if request.method == "GET":
        query = get_object_or_None(Product, pk)
        if query:
            serializer = ProductSerializerGET(query, many=False)
            return ResponseSuccess(serializer.data)
        else:
            return ResponseFail("The ID you sent is incorrect")
    elif request.method == "PUT":
        query = get_object_or_None(Product, pk)
        if query:
            serializer = ProductSerializer(data=request.data, instance=query)
            if serializer.is_valid():
                serializer.save()
                return ResponseSuccess(serializer.data)
            else:
                return ResponseFail("Invalid data")
        else:
            return ResponseFail("The ID you sent is incorrect")
    elif request.method == "Delete":
        query = get_object_or_None(Product, pk)
        if query:
            query.delete()
            return ResponseSuccess("Deleted object")
        else:
            return ResponseFail("The ID you sent is incorrect")

@api_view(['GET', "POST"])
def products_items(request):
    if request.method == "GET":
        query = ProductItems.objects.all()
        serializer = ProductItemsSerializerGET(query, many=True)
        return ResponseSuccess(serializer.data)
    elif request.method == "POST":
        serializer = ProductItemsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseSuccess(serializer.data)

@api_view(['GET', "PUT", "DELETE"])
def product_items(request, pk):
    if request.method == "GET":
        query = get_object_or_None(ProductItems, pk)
        if query:
            serializer = ProductItemsSerializerGET(query, many=False)
            return ResponseSuccess(serializer.data)
        else:
            return ResponseFail("The ID you sent is incorrect")
    elif request.method == "PUT":
        query = get_object_or_None(ProductItems, pk)
        if query:
            serializer = ProductItemsSerializer(data=request.data, instance=query)
            if serializer.is_valid():
                serializer.save()
                return ResponseSuccess(serializer.data)
            else:
                return ResponseFail("Invalid data")
        else:
            return ResponseFail("The ID you sent is incorrect")
    elif request.method == "Delete":
        query = get_object_or_None(ProductItems, pk)
        if query:
            query.delete()
            return ResponseSuccess("Deleted object")
        else:
            return ResponseFail("The ID you sent is incorrect")

@api_view(['GET', "POST"])
def categories(request):
    if request.method == "GET":
        query = Category.objects.all()
        serializer = CategorySerializer(query, many=True)
        return ResponseSuccess(serializer.data)
    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseSuccess(serializer.data)

@api_view(['GET', "PUT", "DELETE"])
def category(request, pk):
    if request.method == "GET":
        query = get_object_or_None(Category, pk)
        if query:
            serializer = CategorySerializer(query, many=False)
            return ResponseSuccess(serializer.data)
        else:
            return ResponseFail("The ID you sent is incorrect")
    elif request.method == "PUT":
        query = get_object_or_None(Category, pk)
        if query:
            serializer = CategorySerializer(data=request.data, instance=query)
            if serializer.is_valid():
                serializer.save()
                return ResponseSuccess(serializer.data)
            else:
                return ResponseFail("Invalid data")
        else:
            return ResponseFail("The ID you sent is incorrect")
    elif request.method == "Delete":
        query = get_object_or_None(Category, pk)
        if query:
            query.delete()
            return ResponseSuccess("Deleted object")
        else:
            return ResponseFail("The ID you sent is incorrect")


@api_view(['GET', "POST"])
def orders(request):
    if request.method == "GET":
        query = Order.objects.all()
        serializer = OrderSerializerGET(query, many=True)
        return ResponseSuccess(serializer.data)
    elif request.method == "POST":
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseSuccess(serializer.data)

@api_view(['GET', "PUT", "DELETE"])
def order(request, pk):
    if request.method == "GET":
        query = get_object_or_None(Order, pk)
        if query:
            serializer = OrderSerializerGET(query, many=False)
            return ResponseSuccess(serializer.data)
        else:
            return ResponseFail("The ID you sent is incorrect")
    elif request.method == "PUT":
        query = get_object_or_None(OrderSerializer, pk)
        if query:
            serializer = OrderSerializer(data=request.data, instance=query)
            if serializer.is_valid():
                serializer.save()
                return ResponseSuccess(serializer.data)
            else:
                return ResponseFail("Invalid data")
        else:
            return ResponseFail("The ID you sent is incorrect")
    elif request.method == "Delete":
        query = get_object_or_None(Order, pk)
        if query:
            query.delete()
            return ResponseSuccess("Deleted object")
        else:
            return ResponseFail("The ID you sent is incorrect")
