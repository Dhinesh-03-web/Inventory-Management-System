from rest_framework import serializers
from .models import *

class categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class productserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class labourserializer(serializers.ModelSerializer):
    class Meta:
        model = Labours
        fields = "__all__"

class supplierserializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = "__all__"

class salesreportserializer(serializers.ModelSerializer):
    class Meta:
        model = Salesreport
        fields = "__all__"