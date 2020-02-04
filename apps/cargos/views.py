from django.shortcuts import render
from rest_framework import viewsets
from .models import Cargo, CargoType, CargoBoxType
from .serializers import CargoSerializer, CargoTypeSerializer, CargoBoxTypeSerializer

# Create your views here.


class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.filter(is_assign=False)
    serializer_class = CargoSerializer


class CargoTypeViewSet(viewsets.ModelViewSet):
    queryset = CargoType.objects.all()
    serializer_class = CargoTypeSerializer


class CargoBoxTypeViewSet(viewsets.ModelViewSet):
    queryset = CargoBoxType.objects.all()
    serializer_class = CargoBoxTypeSerializer
