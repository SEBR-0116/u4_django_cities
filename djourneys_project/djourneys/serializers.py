from rest_framework import serializers
from .models import City, Attraction, Review


class CitySerializer(serializers.HyperlinkedModelSerializer):
    attractions = serializers.HyperlinkedRelatedField(
        view_name='attraction_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = City
        fields = ('name', 'country', 'population', 'attractions')


class AttractionSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(
        view_name='review_detail',
        many=True,
        read_only=True,
    )

    class Meta:
        model = Attraction
        fields = ('city', 'name', 'description', 'type', 'reviews')


class ReviewSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Review
        fields = ('attraction', 'title', 'rating', 'content')
