from django.contrib import admin
from .models import Cities, Attraction, Review
# Register your models here.

admin.site.register(Cities)
admin.site.register(Attraction)
admin.site.register(Review)