from rest_framework import serializers
from .models import Cities, Attraction, Review

class ReviewSerializer(serializers.ModelSerializer):
  attraction = serializers.PrimaryKeyRelatedField(
      queryset=Attraction.objects.all(),
      source='attraction_id'
    )
  
  review_url = serializers.ModelSerializer.serializer_url_field(
    view_name = 'reviews-detail',
  )

  class Meta:
    model = Review
    fields = ('id', 'attraction', 'rating', 'guest_photo', 'description', 'review_url')


class AttractionSerializer(serializers.ModelSerializer):
  review = ReviewSerializer(
    many = True,
    read_only = True
  )

  city_url = serializers.HyperlinkedRelatedField(
        view_name='cities-detail',
        source='cities',
        read_only=True
    )


  class Meta:
    model = Attraction
    fields = ('id', 'name', 'url', 'city_url', 'description', 'review')


class CitiesSerializer(serializers.ModelSerializer):
  attraction = AttractionSerializer(
    many=True, 
    read_only=True
  )


  class Meta:
    model = Cities
    fields = ('id', 'name', 'state', 'year_founded', 'city_img', 'attraction')