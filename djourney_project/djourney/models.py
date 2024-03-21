from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length =100)
    country = models.CharField(max_length =100)
    region = models.CharField(max_length =100)
    population = models.IntegerField()
    independentDate = models.DateField()
    gdp = models.FloatField()
    
    def __str__(self):
        return self.name
    
class Attraction(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    session_start_date = models.DateField()
    session_end_date = models.DateField()
    area_in_meters = models.FloatField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='attractions')
    
    def __str__(self):
        return self.name
    
class Review(models.Model):
    Rating_Stars = (
        ('X', 'X'),
        ('XX', 'XX'),
        ('XXX', 'XXX'),
        ('XXXX', 'XXXX'),
        ('XXXXX', 'XXXXX'),
    )
    author = models.CharField(max_length=100)
    rating = models.CharField(max_length=10, choices=Rating_Stars,default="None")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='reviews', default=None) 
    def __str__(self):
        return  f"Review by {self.author} for {self.attraction.name}"