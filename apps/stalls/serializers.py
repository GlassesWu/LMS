from rest_framework import serializers
from .models import Stall


class StallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stall
        fields = ['id', "stallname", "address", "consignee", "phone"]
