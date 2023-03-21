from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Subject(models.Model):
    class YearLevels(models.TextChoices):
        FIRST_YEAR = 'IU-Y1', '1st Year'
        SECOND_YEAR = 'IU-Y2', '2nd Year'
        THIRD_YEAR = 'IU-Y3', '3rd Year'
        FOURTH_YEAR = 'IU-Y4', '4th Year'

    class Semesters(models.TextChoices):
        FIRST_SEM = 'Sem-1', '1st Semester'
        SECOND_SEM = 'Sem-2', '2nd Semester'

    name = models.CharField(max_length=40)
    enrolled_count = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(60),
            MinValueValidator(0)
        ])
    max_slots = models.IntegerField(default=60)
    year_level = models.CharField(max_length=20, choices=YearLevels.choices)
    semester = models.CharField(
        max_length=20, choices=Semesters.choices, default=Semesters.FIRST_SEM)

    def __str__(self):
        return self.name
