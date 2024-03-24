from rest_framework import serializers
from .models import City, Attraction, Review

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    attraction = serializers.HyperlinkedRelatedField(
        view_name='attraction_detail',
        read_only=True
    )
    attraction_id = serializers.PrimaryKeyRelatedField(
        queryset=Attraction.objects.all(),
        source='attraction'
    )
    class Meta:
        model = Review
        fields = ('id', 'attraction_id', 'attraction', 'rating', 'review_title', 'review_description')


class AttractionSerializer(serializers.HyperlinkedModelSerializer):
    reviews = ReviewSerializer(
        many=True,
        read_only=True
    )
    city_id = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(),
        source='city'
    )
    class Meta:
        model = Attraction
        fields = ('id', 'city_id', 'name', 'description', 'image_url', 'city', 'reviews')


class CitySerializer(serializers.HyperlinkedModelSerializer):
    attractions = AttractionSerializer(
        many=True,
        read_only=True
    )
    city_url = serializers.HyperlinkedIdentityField(
        view_name='city-detail'
    )
    class Meta:
        model = City
        fields = ('id', 'city_url', 'name', 'year_founded', 'population', 'image_url', 'attractions')