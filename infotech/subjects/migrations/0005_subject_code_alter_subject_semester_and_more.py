# Generated by Django 4.2 on 2023-04-22 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0004_remove_subject_enrolled_count_subjectstudent_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='code',
            field=models.CharField(default='PLCHLDER-1', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subject',
            name='semester',
            field=models.CharField(choices=[('1st Semester', 'First Sem'), ('2nd Semester', 'Second Sem')], default='1st Semester', max_length=20),
        ),
        migrations.AlterField(
            model_name='subject',
            name='year_level',
            field=models.CharField(choices=[('1st Year', 'First Year'), ('2nd Year', 'Second Year'), ('3rd Year', 'Third Year'), ('4th Year', 'Fourth Year')], max_length=20),
        ),
    ]
