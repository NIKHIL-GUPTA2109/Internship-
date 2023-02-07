from rest_framework import serializers
from .models import Artist, Work

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
    work = WorkSerializer(many=True)

    class Meta:
        model = Artist
        fields = '__all__'
