from .models import Tour
from rest_framework import serializers


class TourSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tour
        fields = ['id', 'location_title', 'description', 'body', 'image']
