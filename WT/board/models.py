from django.db import models

# Create your models here.
class car (models.Model):
    x = [(2020,2020), (2021, 2021), (2022, 2022)]
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    model = models.IntegerField(choices=x)
    price = models.DecimalField(max_digits=9, decimal_places=3)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    def __str__(self):
        return self.name



class customers(models.Model):
    name= models.CharField(max_length=50)
    age = models.IntegerField()
    car_buy = models.ManyToManyField(car)

    def __str__(self):
        return self.name
