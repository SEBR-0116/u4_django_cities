from .serializers import CitiesSerializer, AttractionSerializer, ReviewSerializer
from .models import Cities, Attraction, Review
from rest_framework import generics
from django.shortcuts import render

# Create your views here.

class CityList(generics.ListCreateAPIView):
  queryset = Cities.objects.all()
  serializer_class = CitiesSerializer

class CityDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Cities.objects.all()
  serializer_class = CitiesSerializer

class AttractionList(generics.ListCreateAPIView):
  queryset = Attraction.objects.all()
  serializer_class = AttractionSerializer

class AttractionDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Attraction.objects.all()
  serializer_class = AttractionSerializer

class ReviewList(generics.ListCreateAPIView):
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer
