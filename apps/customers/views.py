from rest_framework import viewsets
from .models import Customer, CustomerLabel
from .serializers import CustomerSerializer, CustomerLabelSerializer

# Create your views here.


class CustomerViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerLabelViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = CustomerLabel.objects.all()
    serializer_class = CustomerLabelSerializer
