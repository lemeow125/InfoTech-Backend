from django.db import models
# Create your models here.


class Student(models.Model):

    class YearLevels(models.TextChoices):
        FIRST_YEAR = 'IU-Y1', '1st Year'
        SECOND_YEAR = 'IU-Y2', '2nd Year'
        THIRD_YEAR = 'IU-Y3', '3rd Year'
        FOURTH_YEAR = 'IU-Y4', '4th Year'

    class Semesters(models.TextChoices):
        FIRST_SEM = 'Sem-1', '1st Semester'
        SECOND_SEM = 'Sem-2', '2nd Semester'

    class SexChoices(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'

    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    #
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=SexChoices.choices)
    birthdate = models.DateField()
    #
    address = models.CharField(max_length=150)
    birthplace = models.CharField(max_length=150)
    #
    mother_name = models.CharField(max_length=80)
    father_name = models.CharField(max_length=80)
    #
    registrar_done = models.BooleanField()
    clearance_done = models.BooleanField()
    pta_done = models.BooleanField()
    #
    # enrolled_subjects = models.ManyToManyField(
    #    'subjects.Subject', through='subjects.SubjectStudent')
    year_level = models.CharField(max_length=20, choices=YearLevels.choices)
    current_semester = models.CharField(
        max_length=20, choices=Semesters.choices, default=Semesters.FIRST_SEM)

    def __str__(self):
        return self.first_name

    @property
    def full_name(self):
        return self.first_name + " " + self.middle_name + " " + self.last_name
