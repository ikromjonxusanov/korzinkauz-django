from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .forms import *
from .serializers import *
from products.models import *
from django.contrib.auth import authenticate, login, logout

@csrf_exempt
@api_view(['POST'])
def user_login(request):
    user = authenticate(
        username=request.data.get('email'),
        password=request.data.get('password')
    )
    if user is None:
        return Response({
            "ok":False,
            "data":"Username and/or password incurrect"
        })
    login(request, user)
    return Response({
        'ok':True,
    })

@api_view(["DELETE"])
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return Response({
            'ok':True
        })


@csrf_exempt
@api_view(['GET', 'POST', "PUT", "DELETE"])
def products(request, pk=None):
    if request.method == "GET":
        if pk:
            queryset = get_object_or_404(Product, pk)
            if queryset:
                serializer = ProductGetFkObjectSerializer(queryset, many=False)
                return Response(serializer.data)
            else:
                return Response({"ok": False, 'data': "The information in the id you provided is not available"})
        else:
            queryset = Product.objects.all()
            serializer = ProductGetFkObjectSerializer(queryset, many=True)
            return Response(serializer.data)
    elif request.method == "POST":
        validated = ProductForm(data=request.data)
        if validated.is_valid():
            serializer = ProductSerializer(data=request.data)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'ok':False, 'data':'The data could not be validated'})
    elif request.method == "PUT":
        if pk:
            queryset = get_object_or_404(Product, pk)
            if queryset:
                validated = ProductForm(instance=queryset, data=request.data)
                if validated.is_valid():
                    serializer = ProductSerializer(instance=queryset, data=request.data)
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response({'ok':False, 'data':'The data could not be validated'})
            else:
                return Response({"ok": False, 'data': "The information in the id you provided is not available"})
        else:
            return Response({"ok": False, 'data': "Not found object id"})
    elif request.method == "DELETE":
        queryset = get_object_or_404(Product, pk)
        if queryset:
            queryset.delete()
            return Response({"deleted object": True})
        else:
            return Response({"ok": False, 'data': "The information in the id you provided is not available"})

@csrf_exempt
@api_view(['GET', 'POST', "PUT", "DELETE"])
def categories(request, pk=None):
    if request.method == "GET":
        if pk:
            queryset = get_object_or_404(Category, pk)
            if queryset:
                serializer = CategorySerializer(queryset, many=False)
                return Response(serializer.data)
            else:
                return Response({"ok": False, 'data': "The information in the id you provided is not available"})
        else:
            queryset = Category.objects.all()
            serializer = CategorySerializer(queryset, many=True)
            return Response(serializer.data)
    elif request.method == "POST":
        validated = CategoryForm(data=request.data)
        if validated.is_valid():
            serializer = CategorySerializer(data=request.data)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'ok': False, 'data': 'The data could not be validated'})
    elif request.method == "PUT":
        if pk:
            queryset = get_object_or_404(Category, pk)
            if queryset:
                validated = CategoryForm(instance=queryset, data=request.data)
                if validated.is_valid():
                    serializer = CategorySerializer(instance=queryset, data=request.data)
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response({'ok': False, 'data': 'The data could not be validated'})
            else:
                return Response({"ok": False, 'data': "The information in the id you provided is not available"})
        else:
            return Response({"ok": False, 'data': "Not found object id"})
    elif request.method == "DELETE":
        queryset = get_object_or_404(Category, pk)
        if queryset:
            queryset.delete()
            return Response({"deleted object": True})
        else:
            return Response({"ok": False, 'data': "The information in the id you provided is not available"})

@csrf_exempt
@api_view(['GET', 'POST', "PUT", "DELETE"])
def statuses(request, pk=None):
    if request.method == "GET":
        if pk:
            queryset = get_object_or_404(Status, pk)
            if queryset:
                serializer = StatusSerializer(queryset, many=False)
                return Response(serializer.data)
            else:
                return Response({"ok": False, 'data': "The information in the id you provided is not available"})
        else:
            queryset = Status.objects.all()
            serializer = StatusSerializer(queryset, many=True)
            return Response(serializer.data)
    elif request.method == "POST":
        validated = StatusForm(data=request.data)
        if validated.is_valid():
            serializer = StatusSerializer(data=request.data)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'ok': False, 'data': 'The data could not be validated'})
    elif request.method == "PUT":
        if pk:
            queryset = get_object_or_404(Status, pk)
            if queryset:
                validated = StatusForm(instance=queryset, data=request.data)
                if validated.is_valid():
                    serializer = StatusSerializer(instance=queryset, data=request.data)
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response({'ok': False, 'data': 'The data could not be validated'})
            else:
                return Response({"ok": False, 'data': "The information in the id you provided is not available"})
        else:
            return Response({"ok": False, 'data': "Not found object id"})
    elif request.method == "DELETE":
        queryset = get_object_or_404(Status, pk)
        if queryset:
            queryset.delete()
            return Response({"deleted object": True})
        else:
            return Response({"ok": False, 'data': "The information in the id you provided is not available"})

@csrf_exempt
@api_view(['GET', 'POST', "PUT", "DELETE"])
def customers(request, pk=None):
    if request.method == "GET":
        if pk:
            queryset = get_object_or_404(Customer, pk)
            if queryset:
                serializer = CustomerGetFkObjectSerializer(queryset, many=False)
                return Response(serializer.data)
            else:
                return Response({"ok": False, 'data': "The information in the id you provided is not available"})
        else:
            queryset = Product.objects.all()
            serializer = ProductGetFkObjectSerializer(queryset, many=True)
            return Response(serializer.data)
    elif request.method == "POST":
        validated = CustomerForm(data=request.data)
        if validated.is_valid():
            serializer = CustomerSerializer(data=request.data)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'ok':False, 'data':'The data could not be validated'})
    elif request.method == "PUT":
        if pk:
            queryset = get_object_or_404(Customer, pk)
            if queryset:
                validated = CustomerForm(instance=queryset, data=request.data)
                if validated.is_valid():
                    serializer = CustomerSerializer(instance=queryset, data=request.data)
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response({'ok':False, 'data':'The data could not be validated'})
            else:
                return Response({"ok": False, 'data': "The information in the id you provided is not available"})
        else:
            return Response({"ok": False, 'data': "Not found object id"})
    elif request.method == "DELETE":
        queryset = get_object_or_404(Customer, pk)
        if queryset:
            queryset.delete()
            return Response({"deleted object": True})
        else:
            return Response({"ok": False, 'data': "The information in the id you provided is not available"})

@csrf_exempt
@api_view(['GET', 'POST', "PUT", "DELETE"])
def orders(request, pk=None):
    if request.method == "GET":
        if pk:
            queryset = get_object_or_404(Order, pk)
            if queryset:
                serializer = OrderGetFkObjectSerializer(queryset, many=False)
                return Response(serializer.data)
            else:
                return Response({"ok": False, 'data': "The information in the id you provided is not available"})
        else:
            queryset = Order.objects.all()
            serializer = OrderGetFkObjectSerializer(queryset, many=True)
            return Response(serializer.data)
    elif request.method == "POST":
        validated = OrderForm(data=request.data)
        if validated.is_valid():
            serializer = OrderSerializer(data=request.data)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'ok':False, 'data':'The data could not be validated'})
    elif request.method == "PUT":
        if pk:
            queryset = get_object_or_404(Order, pk)
            if queryset:
                validated = OrderForm(instance=queryset, data=request.data)
                if validated.is_valid():
                    serializer = OrderSerializer(instance=queryset, data=request.data)
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response({'ok':False, 'data':'The data could not be validated'})
            else:
                return Response({"ok": False, 'data': "The information in the id you provided is not available"})
        else:
            return Response({"ok": False, 'data': "Not found object id"})
    elif request.method == "DELETE":
        queryset = get_object_or_404(Order, pk)
        if queryset:
            queryset.delete()
            return Response({"deleted object": True})
        else:
            return Response({"ok": False, 'data': "The information in the id you provided is not available"})
