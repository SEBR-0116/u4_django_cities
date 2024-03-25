from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    population=models.IntegerField()
    founded_year=models.IntegerField()

 
    def __str__(self):
        return self.name

class Attraction(models.Model):
     name = models.CharField(max_length=100)
     location= models.CharField(max_length=100)
     city=models.ForeignKey(City, on_delete=models.CASCADE, related_name='atracctions')
     
     def __str__(self):
        return self.name



class Review(models.Model):
    name = models.CharField(max_length=100)
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='reviews')
    stars=models.IntegerField()
    name_of_reviewer=models.CharField(max_length=100)
    email_of_reviewer=models.EmailField()
    will_be_coming_back=models.BooleanField()

    
    def __str__(self):
        return self.name
     