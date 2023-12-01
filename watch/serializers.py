from rest_framework import serializers
from .models import Watch

class WatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watch
        fields = ['id', 'name', 'model', 'brand', 'description', 'type', 'is_mine', 'main_image', 'second_image']