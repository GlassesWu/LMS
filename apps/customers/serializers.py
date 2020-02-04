from rest_framework import serializers
from .models import Customer, CustomerLabel


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['uid', 'name', 'mobile_phone']


class CustomerLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerLabel
        fields = ['id', 'customer', 'labelname']
