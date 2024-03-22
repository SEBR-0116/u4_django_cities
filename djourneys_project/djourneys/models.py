from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Attraction(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='attractions')

    def __str__(self):
        return self.name

class Review(models.Model):
    text = models.TextField()
    rating = models.IntegerField()
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='reviews')
    
    def __str__(self):
        return f"Review for {self.attraction.name}"