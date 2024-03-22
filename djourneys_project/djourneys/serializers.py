from rest_framework import serializers
from .models import City, Attraction, Review

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    attraction = serializers.HyperlinkedRelatedField(
        view_name='attraction-detail',
        read_only=True
    )

    attraction_id = serializers.PrimaryKeyRelatedField(
        queryset = Attraction.objects.all(),
        source='attraction'
    )

    class Meta:
        model = Review
        # fields = ('id', 'attraction', 'attraction_id', 'content')
        fields = ('__all__')

class AttractionSerializer(serializers.HyperlinkedModelSerializer):
    city = serializers.HyperlinkedRelatedField(
        view_name='city_detail',
        read_only=True
    )

    reviews = ReviewSerializer(
        many=True,
        read_only=True
    )

    city_id = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(),
        source='city'
    )

    attraction_url = serializers.ModelSerializer.serializer_url_field(
        view_name='attraction-detail'
    )

    class Meta:
        model = Attraction
        fields = ('id', 'name', 'attraction_url', 'city', 'city_id', 'photo_url', 'reviews')

class CitySerializer(serializers.HyperlinkedModelSerializer):
    attractions = AttractionSerializer(
        many=True,
        read_only=True
    )

    city_url = serializers.ModelSerializer.serializer_url_field(
        view_name='city_detail'
    )

    class Meta:
        model = City
        fields = ('id', 'city_url','name', 'state', 'country', 'continent', 'attractions')
