# Generated by Django 4.2 on 2023-04-22 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0002_alter_schedule_professor'),
        ('students', '0005_remove_student_enrolled_subjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='schedules',
            field=models.ManyToManyField(through='schedules.StudentSchedule', to='schedules.schedule'),
        ),
    ]
