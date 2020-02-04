from rest_framework import serializers
from .models import ManifestInfo, Manifest


class ManifestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manifest
        fields = ['uuid', 'created_date', 'truck_number', 'trucker', 'trucker_phone', 'stall_phone', 'destination',
                  'total_quantity', 'total_price', 'truckage', 'deadweight', 'weight_unit', 'overweight',
                  'overweight_cost', 'cartage', 'cartage', 'prepay', 'created_time', 'updated_time']


class ManifestInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManifestInfo
        fields = ['id', 'uuid', 'stallname', 'cargo', 'label', 'type', 'box', 'quantity', 'unit_price', 'price',
                  'is_output', 'is_paycollect', 'created_time', 'updated_time', 'detail']
