from django.contrib import admin

# Register your models here.

from .models import Citie, Attraction, Review
admin.site.register(Citie)
admin.site.register(Attraction)
admin.site.register(Review)