from api.models import Category, Order, Product, ProductItems, UserModel
from django_filters import FilterSet, NumberFilter, CharFilter



class ProductFilter(FilterSet):
    price_min = NumberFilter(field_name="price", lookup_expr="lte")
    price_max = NumberFilter(field_name="price", lookup_expr="gte")
    name = CharFilter(field_name="name", lookup_expr="icontains")
    quantities_min = NumberFilter(field_name="quantities", lookup_expr="lte")
    quantities_max = NumberFilter(field_name="quantities", lookup_expr="gte")
    create_date_start = NumberFilter(field_name="create_date", lookup_expr="lte")
    create_date_end = NumberFilter(field_name="create_date", lookup_expr="gte")
    duedate_start = NumberFilter(field_name="duedate", lookup_expr="lte")
    duedate_end = NumberFilter(field_name="duedate", lookup_expr="gte")
    code = CharFilter(field_name="code", lookup_expr="icontains")
    class Meta:
        model = Product
        fields = ['category']

class ProductItemsFilter(FilterSet):
    quantities_min = NumberFilter(field_name="price", lookup_expr="lte")
    quantities_max = NumberFilter(field_name="price", lookup_expr="gte")
    sub_price_min = NumberFilter(field_name="quantities", lookup_expr="lte")
    sub_price_max = NumberFilter(field_name="quantities", lookup_expr="gte")
    create_date_start = NumberFilter(field_name="duedate", lookup_expr="lte")
    create_date_end = NumberFilter(field_name="duedate", lookup_expr="gte")
    class Meta:
        model = ProductItems
        fields = ['product']

class OrderFilter(FilterSet):

    code_min = NumberFilter(field_name="code", lookup_expr="lte")
    code_max = NumberFilter(field_name="code", lookup_expr="gte")
    sub_price_min = NumberFilter(field_name="sub_price", lookup_expr="lte")
    sub_price_max = NumberFilter(field_name="sub_price", lookup_expr="gte")
    orderTime_min = NumberFilter(field_name="orderTime", lookup_expr="lte")
    orderTime_max = NumberFilter(field_name="orderTime", lookup_expr="gte")
    date_min = NumberFilter(field_name="date", lookup_expr="lte")
    date_max = NumberFilter(field_name="date", lookup_expr="gte")
    create_date_min = NumberFilter(field_name="create_date", lookup_expr="lte")
    create_date_max = NumberFilter(field_name="create_date", lookup_expr="gte")
    class Meta:
        model = Order
        fields = ['products', "status"]

class CategoryFilter(FilterSet):
    name = CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Category
        fields = ["description"]

class UserFilter(FilterSet):
    email = CharFilter(field_name="email", lookup_expr="icontains")
    first_name = CharFilter(field_name="first_name", lookup_expr="icontains")
    last_name = CharFilter(field_name="last_name", lookup_expr="icontains")
    phone_number = CharFilter(field_name="phone_number", lookup_expr="icontains")
    passport_code = CharFilter(field_name="passport_code", lookup_expr="icontains")
    class Meta:
        model = UserModel
        fields = ["user_type"]

