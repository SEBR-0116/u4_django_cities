from rest_framework import serializers
from .models import City,Attraction,Review

class CitySerializer(serializers.HyperlinkedModelSerializer):
    attractions = serializers.HyperlinkedRelatedField(
        view_name = 'attraction_detail',
        many=True,
        read_only=True
    )
    
    class Meta:
        model = City
        fields = ('id','name','country','region','population','independentDate','gdp','attractions',)
        
class AttractionSerializer(serializers.HyperlinkedModelSerializer):
    city = serializers.HyperlinkedRelatedField(
        view_name='city_detail',
        read_only = True
    )
    
    reviews = serializers.HyperlinkedIdentityField(
        view_name='review_detail',
        many=True,
        read_only = True
    )
    
    class Meta:
        model = Attraction
        fields = ('id','name','description','session_start_date','session_end_date','area_in_meters','city','reviews',)
        
class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    attraction = serializers.HyperlinkedIdentityField(
        view_name='attraction_detail',
        read_only=True
    )
    
    class Meta:
        model = Review
        fields = ('id','author','rating','comment','created_at','attraction',)