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
    review_url = serializers.ModelSerializer.serializer_url_field(
        view_name='review_detail'
    )

    class Meta:
        model = Review
        fields = ('id', 'review_url', 'attraction', 'attraction_id', 'reviewer', 'comment', 'date_of_review')
        
 
class AttractionSerializer(serializers.HyperlinkedModelSerializer):
    reviews = ReviewSerializer(
        many = True,
        read_only = True
    )
    attraction_url = serializers.ModelSerializer.serializer_url_field(
        view_name='attraction_detail'
    )
    # -------
    city = serializers.HyperlinkedRelatedField(
        view_name='city_detail',
        read_only=True
    )

    city_id = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(),
        source='city'
    )
    class Meta:
        model = Attraction
        fields = ('id', 'attraction_url', 'street_address', 'city', 'city_id', 'description', 'hours_of_operation','average_fee', 'reviews')

class CitySerializer(serializers.HyperlinkedModelSerializer):
    attractions = AttractionSerializer(
        many = True,
        read_only = True
    )
    city_url = serializers.ModelSerializer.serializer_url_field(
        view_name='city_detail'
   )
    class Meta:
        model = City
        fields = ('id', 'city_url', 'name', 'state_or_other', 'country', 'population', 'attractions')