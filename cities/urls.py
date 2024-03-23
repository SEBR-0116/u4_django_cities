# from django.urls import path
# from . import views
# from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('cities/', views.CityList.as_view(), name='city_list'),
#     path('cities/<int:pk>/', views.CityDetail.as_view(), name='city_detail'),
#     path('attractions/', views.AttractionList.as_view(), name='attraction_list'),
#     path('attractions/<int:pk>/', views.AttractionDetail.as_view(), name='attraction_detail'),
#     path('reviews/', views.ReviewList.as_view(), name='review_list'),
#     path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review_detail'),
# ]

from django.conf.urls import include
from django.urls import path
from .views import CityList, CityDetail, AttractionList, AttractionDetail, ReviewList, ReviewDetail
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('cities/', CityList.as_view(), name='city-list'),
    path('cities/<int:pk>/', CityDetail.as_view(), name='city-detail'),
    path('attractions/', AttractionList.as_view(), name='attraction-list'),
    path('attractions/<int:pk>/', AttractionDetail.as_view(), name='attraction-detail'),
    path('reviews/', ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
]

