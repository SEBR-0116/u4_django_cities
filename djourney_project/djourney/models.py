from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)
    state_or_other = models.CharField(max_length=100)
    country = models.CharField(max_length=200)
    population = models.IntegerField()

    def __str__(self):
        return self.name

class Attraction(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='attractions')
    street_address = models.CharField(max_length=100)
    description = models.TextField()
    hours_of_operation = models.TextField()
    average_fee = models.IntegerField()

    def __str__(self):
        return self.name

class Review(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.CharField(max_length=100)
    comment = models.TextField()
    date_of_review = models.DateField()

    def __str__(self):
        return self.reviewer