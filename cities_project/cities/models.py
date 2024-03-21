from django.db import models

# Create your models here.
class Citie(models.Model):
  name = models.CharField(max_length=20)
  year_founded = models.IntegerField()
  population = models.IntegerField()
  image_url = models.TextField()

  def __str__(self):
    return self.name

class Attraction(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  image_url = models.TextField()
  citie = models.ForeignKey(Citie, on_delete=models.CASCADE, related_name ='attractions')
  
  def __str__(self):
    return self.name

class Review(models.Model):
  attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='review')
  rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
  review_title = models.TextField(default='')
  review_description = models.TextField(default='')

  def __str__(self):
    return f'{self.attraction.name} - {self.review_title}'