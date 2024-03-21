from django.contrib import admin

# Register your models here.

from .models import City, Attraction,Review
admin.site.register(City)
admin.site.register(Attraction)
admin.site.register(Review)