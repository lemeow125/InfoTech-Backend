from django.db import models
from django.utils.timezone import now

# Create your models here.


class Schedule(models.Model):
    subject = models.ForeignKey('subjects.Subject', on_delete=models.CASCADE)
    students_assigned = models.ManyToManyField(
        'students.Student', related_name='StudentSchedule_student_assigned', through='schedules.StudentSchedule')
    professor = models.OneToOneField(
        'professors.Professor', related_name='Professor_full_name', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=now, editable=False)

    @property
    def name(self):
        return f"{self.subject}"

    def __str__(self):
        return self.subject


class StudentSchedule(models.Model):
    schedule = models.ForeignKey(
        'schedules.Schedule', on_delete=models.CASCADE)
    student_assigned = models.ForeignKey(
        'students.Student', on_delete=models.CASCADE)
    date_joined = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.schedule
