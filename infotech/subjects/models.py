from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import now
# Create your models here.


class Subject(models.Model):
    class YearLevels(models.TextChoices):
        FIRST_YEAR = '1st Year'
        SECOND_YEAR = '2nd Year'
        THIRD_YEAR = '3rd Year'
        FOURTH_YEAR = '4th Year'

    class Semesters(models.TextChoices):
        FIRST_SEM = 'Sem-1', '1st Semester'
        SECOND_SEM = 'Sem-2', '2nd Semester'

    name = models.CharField(max_length=40)
    max_slots = models.IntegerField(default=60)
    year_level = models.CharField(max_length=20, choices=YearLevels.choices)
    semester = models.CharField(
        max_length=20, choices=Semesters.choices, default=Semesters.FIRST_SEM)

    students = models.ManyToManyField(
        'students.Student', related_name='SubjectStudent_student_assigned', through='subjects.SubjectStudent')

    def __str__(self):
        return self.name


class SubjectStudent(models.Model):
    subject = models.ForeignKey('subjects.Subject', on_delete=models.CASCADE)
    student_assigned = models.ForeignKey(
        'students.Student', on_delete=models.CASCADE, null=True)
    date_joined = models.DateTimeField(default=now, editable=False)
