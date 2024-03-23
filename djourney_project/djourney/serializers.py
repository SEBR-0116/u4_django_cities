from rest_framework import serializers
from .models import City,Attraction,Review

       
class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    attraction = serializers.HyperlinkedIdentityField(
        view_name='attraction_detail',
        read_only=True
    )
    
    attraction_id = serializers.PrimaryKeyRelatedField(
        queryset = Attraction.objects.all(),
        source = 'attraction'
    )
        
    class Meta:
        model = Review
        fields = ('id','author','rating','comment','created_at','attraction_id','attraction',)
        

        
class AttractionSerializer(serializers.HyperlinkedModelSerializer):
    city = serializers.HyperlinkedRelatedField(
        view_name='city_detail',
        read_only = True
    )
    
    reviews = ReviewSerializer(
        # view_name='review_detail',
        many=True,
        read_only = True
    )
    
    city_id = serializers.PrimaryKeyRelatedField(
        queryset = City.objects.all(),
        source = 'city'
    )
    
    Attraction_url =  serializers.ModelSerializer.serializer_url_field(
        view_name='attraction_detail'
    )
    
    class Meta:
        model = Attraction
        fields = ('id','name','city_id','Attraction_url','description','session_start_date','session_end_date','area_in_meters','city','reviews',)
         


class CitySerializer(serializers.HyperlinkedModelSerializer):
    attractions = AttractionSerializer(
        # view_name = 'attraction_detail',
        many=True,
        read_only=True
    )
    
    city_url= serializers.ModelSerializer.serializer_url_field(
        view_name='city_detail'
    )
    
    class Meta:
        model = City
        fields = ('id','city_url','name','country','region','population','independentDate','gdp','attractions',)
