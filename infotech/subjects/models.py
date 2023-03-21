from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=40)
    enrolled_count = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(60),
            MinValueValidator(0)
        ])
    max_slots = models.IntegerField(default=60)
    year_level = models.CharField(max_length=20)

    def __str__(self):
        return self.name
