from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)
    year_founded = models.PositiveIntegerField()
    population = models.PositiveIntegerField()
    image_url = models.TextField()

    def __str__(self):
        return self.name
    
class Attraction(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return self.name

class Review(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='attractions')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review_title = models.CharField(max_length=100)
    review_description = models.TextField()

    def __str__(self):
        return f"{self.attraction.name}"

