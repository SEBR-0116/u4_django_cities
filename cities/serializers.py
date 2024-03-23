from rest_framework import serializers
from .models import City, Attraction, Review


class CitySerializer(serializers.HyperlinkedModelSerializer):
    attractions = serializers.HyperlinkedRelatedField(
        view_name='attraction-detail',
        many=True,
        read_only=True
    )
    
    class Meta:
        model = City
        fields = ('id', 'name', 'year_founded', 'population', 'image_url', 'attractions')

class AttractionSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(
        view_name='review-detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Attraction
        fields = ('id', 'name', 'description', 'image_url', 'city', 'reviews')

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'attraction', 'rating', 'review_title', 'review_description')