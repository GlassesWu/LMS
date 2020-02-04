# from django.shortcuts import render
from .models import Storage
from .serializers import StorageSerializer
from rest_framework import viewsets

# Create your views here.


class StorageViewSet(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
