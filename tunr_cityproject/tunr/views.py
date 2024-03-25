from django.shortcuts import render
from rest_framework import generics
from .models import City, Attraction, Review
from .serializers import CitySerializer, AttractionSerializer, ReviewSerializer

class CityList(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityDetail(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class AttractionList(generics.ListAPIView):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer

class AttractionDetail(generics.RetrieveAPIView):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer

class ReviewList(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

