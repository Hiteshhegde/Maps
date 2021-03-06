from django.db import models

# Create your models here.
class Distance(models.Model):

    location = models.CharField(max_length=120, default='Los Angeles')
    destination = models.CharField(max_length=120, default='New York')
    distance = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return f"Distance from { self.location } to { self.destination} is {self.distance} km"