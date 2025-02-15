from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Musician(models.Model):
    name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    salary = models.IntegerField(default=0,validators=[MinValueValidator(0)])

    def __str__(self):
        return f"Name: {self.name}, Instremant: {self.instrument},age: {self.age},salary: {self.salary}"