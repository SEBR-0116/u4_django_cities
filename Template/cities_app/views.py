from django.shortcuts import render # not using but might preload
from rest_framework import generics
from .serializers import CitySerializer, AttractionSerializer, ReviewSerializer
from .models import City, Attraction, Review

# Views
class CityList(generics.ListCreateAPIView): # CRUD: view or add only
    queryset = City.objects.all()
    serializer_class = CitySerializer
class CityDetail(generics.RetrieveUpdateDestroyAPIView): # CRUD: view, edit, & delete but not add
    queryset = City.objects.all()
    serializer_class = CitySerializer

class AttractionList(generics.ListCreateAPIView): # CRUD: view, add
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
class AttractionDetail(generics.RetrieveUpdateDestroyAPIView): # CRUD: view, edit, delete
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer

# Would like the review list to be solely associated with each attraction; only the set of reviews associated w that attraction would show at a time, not a full list of unconnected reviews
class ReviewList(generics.ListCreateAPIView): # CRUD: view, add
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer