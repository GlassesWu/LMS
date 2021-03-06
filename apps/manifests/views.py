from rest_framework.response import Response
from rest_framework import viewsets
from .models import Manifest, ManifestInfo
from .serializers import ManifestSerializer, ManifestInfoSerializer

# Create your views here.


class ManifestViewSet(viewsets.ModelViewSet):
    queryset = Manifest.objects.all()
    serializer_class = ManifestSerializer


class ManifestInfoViewSet(viewsets.ModelViewSet):
    queryset = ManifestInfo.objects.all()
    serializer_class = ManifestInfoSerializer

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
