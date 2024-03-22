from rest_framework import serializers

from .models import City, Attraction,Review

class CitySerializer(serializers.HyperlinkedModelSerializer):
    attraction = serializers.HyperlinkedRelatedField(
        view_name='attraction_detail',
        many=True,
        read_only=True
    )
    
    class Meta:
        model = City
        fields = ('id', 'country', 'name', 'description','attraction')

class AttractionSerializer(serializers.HyperlinkedModelSerializer):
    city = serializers.HyperlinkedRelatedField(
        view_name='city_detail',
        read_only=True
    )
    class Meta:
        model = Attraction
        fields = ('id','name', 'description', 'city')

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    attraction = serializers.HyperlinkedRelatedField(
        view_name='attraction_detail',
        read_only=True
    )
    class Meta:
        model = Review
        fields = ('id', 'text', 'rating', 'attraction')