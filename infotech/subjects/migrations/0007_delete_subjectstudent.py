# Generated by Django 4.2 on 2023-04-22 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_remove_student_enrolled_subjects'),
        ('subjects', '0006_remove_subject_students'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SubjectStudent',
        ),
    ]
