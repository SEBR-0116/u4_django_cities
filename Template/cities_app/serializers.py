from rest_framework import serializers
from .models import City, Attraction, Review

# Start w Child first, then Parents (opposite of Models)

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    attraction = serializers.HyperlinkedRelatedField(
        view_name = 'attraction_detail',
        read_only = True
    )
    attraction_id = serializers.PrimaryKeyRelatedField(
        queryset = Attraction.objects.all(),
        source = 'attraction'
    )
    
    class Meta:
        model = Review
        fields = ('attraction', 'review_name', 'review_rating', 'review_author', 'review_description', 'would_recommend')

class AttractionSerializer(serializers.HyperlinkedModelSerializer):
    review = ReviewSerializer(
        many = True,
        read_only = True
    )
    review_url = serializers.ModelSerializer.serializer_url_field(
        view_name='review_detail'
    )

    # Would you also have to feature City stuff here bc of overlap?
    city = serializers.HyperlinkedRelatedField(
        view_name = 'city_detail',
        read_only = True
    )
    city_id = serializers.PrimaryKeyRelatedField(
        queryset = City.objects.all(),
        source = 'city'
    )
    # Comment ^ out if breaks

    class Meta:
        model = Attraction
        fields = ('city', 'attraction_name', 'attraction_type', 'attraction_img', 'attraction_description')

class CitySerializer(serializers.HyperlinkedModelSerializer):
    attractions = AttractionSerializer(
        many=True,
        read_only=True
    )
    attraction_url = serializers.ModelSerializer.serializer_url_field(
        view_name='attraction_detail'
    )

    class Meta:
        model = City
        fields = ('city_name', 'country_name', 'city_img')