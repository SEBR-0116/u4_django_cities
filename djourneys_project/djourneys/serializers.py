from rest_framework import serializers
from .models import City, Attraction, Review


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    attractions = serializers.HyperlinkedRelatedField(
        view_name='attraction_detail',
        read_only=True
    )

    review = serializers.HyperlinkedIdentityField(
        view_name='review_detail'
    )

    class Meta:
        model = Review
        fields = ('id', 'attractions', 'review', 'title', 'rating', 'content')


class AttractionSerializer(serializers.HyperlinkedModelSerializer):
    city = serializers.HyperlinkedRelatedField(
        view_name='review_detail',
        read_only=True,
    )

    reviews = serializers.HyperlinkedRelatedField(
        view_name='review_detail',
        many=True,
        read_only=True,
    )
    attraction_url = serializers.HyperlinkedIdentityField(
        view_name='attraction_detail')

    class Meta:
        model = Attraction
        fields = ('id', 'attraction_url', 'city', 'name',
                  'description', 'type', 'reviews')


class CitySerializer(serializers.HyperlinkedModelSerializer):
    attractions = serializers.HyperlinkedRelatedField(
        view_name='attraction_detail',
        many=True,
        read_only=True,
    )
    city_url = serializers.HyperlinkedIdentityField(view_name='city_detail')

    class Meta:
        model = City
        fields = ('id', 'city_url', 'name', 'country',
                  'population', 'attractions')
