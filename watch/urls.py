from .api import WatchViewSet
from rest_framework import routers

routers = routers.DefaultRouter()

routers.register('api/watch', WatchViewSet, 'watchs')

urlpatterns = routers.urls