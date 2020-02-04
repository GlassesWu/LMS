from rest_framework import viewsets
from .serializers import StallSerializer
from .models import Stall


# Create your views here.


class StallViewSet(viewsets.ReadOnlyModelViewSet):
    """
    档口信息
    """
    queryset = Stall.objects.all()
    serializer_class = StallSerializer
