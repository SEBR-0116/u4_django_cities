from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100)
    state_name = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__ (self):
        return self.name


class Attraction(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='cities')
    name = models.CharField(max_length=100)
    photo_url = models.TextField()
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Review(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='reviews', null=True)
    title = models.CharField(max_length=100, default='no review title')
    description = models.CharField(max_length=100, default='no review description')

    def __str__(self):
        return self.title