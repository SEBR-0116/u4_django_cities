# Start w Parents first, then Children (reverse of Serializers)

class City(models.Model):
    city_name = models.CharField(max_length=100, default = 'undefined')
    country_name = models.CharField(max_length=100, default = 'undefined')
    city_img = models.TextField(default = 'undefined')
    
    def __str__(self):
        return self.city_name

class Attraction(models.Model):
    # Foreign Key links child to parent
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city')
    attraction_name = models.CharField(max_length=100, default = 'undefined')
    attraction_type = models.CharField(max_length=100, default = 'undefined')
    attraction_img = models.TextField(default = 'undefined')
    attraction_description = models.TextField(default = 'undefined')

    def __str__(self):
        return self.attraction_name

class Review(models.Model):
    # Foreign Key links child to parent
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='attraction')
    review_name = models.CharField(max_length=100, default = 'undefined')
    review_rating = models.CharField(max_length=100, default = 'undefined')
    review_author = models.CharField(max_length=100, default = 'undefined')
    review_description = models.TextField(default = 'undefined')
    would_recommend = models.BooleanField(default=True) # not 100% on this

    def __str__(self):
        return self.review_name
    
# Not sure if you need all the default stuff, but just in case, this should work