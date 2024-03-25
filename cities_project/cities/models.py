from django.db import models

# Create your models here.

class Cities(models.Model):
  name = models.CharField(max_length=100, default='no city name')
  state = models.CharField(max_length=100, default='no state name')
  year_founded = models.CharField(max_length=100, default='no year found')
  city_img = models.TextField(max_length=300, default='no image url', null=True)

  def __str__(self):
    return self.name
  
class Attraction(models.Model):
  cities = models.ForeignKey(Cities, on_delete=models.CASCADE, related_name='attraction')
  name = models.CharField(max_length=100, default='no decade name')
  description = models.TextField(max_length=500, default='no description')
  attraction_img = models.CharField(max_length=250, default='no attraction image')

  def __str__(self):
    return self.name
  
class Review(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    ]

    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='review')
    rating = models.IntegerField(choices=RATING_CHOICES, default=5)
    guest_photo = models.ImageField(upload_to='guest_photos/', null=True, blank=True)
    description = models.CharField(max_length=250, default='no description')

    def __str__(self):
      return f'{self.attraction.name} - {self.rating}'