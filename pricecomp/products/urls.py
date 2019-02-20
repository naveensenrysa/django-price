from django.urls import path, include
from products.views import *
from rest_framework import views

from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter()
router.register('api/v1/products', ProductModelView)
router.register('api/v1/prices', PriceModelAPIView)



ndhproducts_list_view = ProductModelView.as_view({
    "get": "list",
    "post": "create",
})

price_list_view = PriceModelAPIView.as_view({
    "get": "list",
    "post": "create",
})

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/sc/', ScrapeAPIView.as_view()),
    path('api/v1/sc/<int:id>/', ScrapeDetailAPIView.as_view())
]