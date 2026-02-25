from rest_framework import serializers
from .models import Vendor,Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta :

        model = Product

        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Vendor

        fields = '__all__'