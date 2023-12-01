from .models import Watch
from .serializers import WatchSerializer
from rest_framework import viewsets, permissions

class WatchViewSet(viewsets.ModelViewSet):
    queryset = Watch.objects.all()
    serializer_class = WatchSerializer
    permission_classes = [ permissions.AllowAny ]