from django.shortcuts import render
from rest_framework import generics
from .serializers import CitySerializer, AttractionSerializer, ReviewSerializer
from .models import City, Attraction, Review

# Create your views here.

# in our index route we can Read(list) and Create


class CityList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

# in our detail routes we can Read(retrieve), Update, and Delete


class CityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


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
