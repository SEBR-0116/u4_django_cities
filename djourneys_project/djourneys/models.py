from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    population = models.IntegerField()

    def __str__(self):
        return self.name


class Attraction(models.Model):
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='attractions')
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=100)
    photo_url = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    attraction = models.ForeignKey(
        Attraction, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=100)
    rating = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return self.title
