from rest_framework import routers
from api.views import ProductsViewSet, ProductsItemsViewSet, CategoriesViewSet, OrdersViewSet, UsersViewSet
router = routers.DefaultRouter()
router.register("products", ProductsViewSet, basename="products"),
router.register("products-items", ProductsItemsViewSet, basename="products-items"),
router.register("categories", CategoriesViewSet, basename="categories"),
router.register("orders", OrdersViewSet, basename="orders"),
router.register("users", UsersViewSet, basename="users"),