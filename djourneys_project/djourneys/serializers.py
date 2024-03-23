from rest_framework import serializers
from .models import City, Attraction, Review

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    attraction = serializers.HyperlinkedRelatedField(
        view_name='attraction_detail',
        read_only = True
    )

    attraction_id = serializers.PrimaryKeyRelatedField(
        queryset = Attraction.objects.all(),
        source = 'attraction'
    )

    review_url = serializers.ModelSerializer.serializer_url_field(
        view_name = 'review_detail'
    )

    class Meta:
        model = Review
        fields = ('id', 'review_url', 'attraction', 'attraction_id', 'reviewer', 'rating', 'reviewer')


class AttractionSerializer(serializers.HyperlinkedModelSerializer):
    review = ReviewSerializer(
        many = True,
        read_only = True
    )

    city = serializers.HyperlinkedRelatedField(
        view_name='city_detail',
        read_only = True
    )

    city_id = serializers.PrimaryKeyRelatedField(
        queryset = City.objects.all(),
        source = 'city'
    )

    attraction_url = serializers.ModelSerializer.serializer_url_field(
        view_name = 'attraction_detail'
    )

    class Meta:
        model = Attraction
        fields = ('id', 'attraction_url', 'name', 'neighbourhood', 'city', 'city_id', 'type', 'free', 'price_adult', 'description', 'website', 'review')

class CitySerializer(serializers.HyperlinkedModelSerializer):
    attraction = AttractionSerializer(
        many = True,
        read_only = True
    )

    city_url = serializers.ModelSerializer.serializer_url_field(
        view_name='city_detail'
    )

    class Meta:
        model = City
        fields = ('id', 'city_url', 'name', 'country','int_airports', 'attraction',)