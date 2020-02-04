from rest_framework import serializers
from .models import Cargo,  CargoType, CargoBoxType


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ['uuid', 'type', 'box', 'quantity', 'customerlabel', 'address', 'is_split',
                  'parent_uuid', 'is_assign', 'created_time', 'updated_time']


class CargoTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CargoType
        fields = ['id', 'typeid', 'typename']


class CargoBoxTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CargoBoxType
        fields = ['id', 'typeid', 'typename']
