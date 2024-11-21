from django.urls import path
from . import views

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'products')
urlpatterns = [
    path('', views.products, name='products'),
]
