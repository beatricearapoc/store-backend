#import serializer from rest framework
from rest_framework import serializers

#import model from models.py
from .models import Product

#Create a model serializer
class ProductSerializer(serializers.ModelSerializer):
    #Specify models and fields
    class Meta:
        model = Product
        fields = ('id','title','price','description')