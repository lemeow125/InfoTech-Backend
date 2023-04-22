from rest_framework import serializers
from .models import Schedule
from professors.models import Professor
from subjects.models import Subject
from students.models import Student


class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    date_created = serializers.DateTimeField(
        format="%d-%m-%Y %I:%M%p", read_only=True)

    # students_assigned = serializers.SlugRelatedField(
    # queryset=Student.objects.all(), slug_field='student_assigned', allow_null=True)

    professor = serializers.SlugRelatedField(
        queryset=Professor.objects.all(), slug_field='full_name', allow_null=True)

    subject = serializers.SlugRelatedField(
        queryset=Subject.objects.all(), slug_field='code', allow_null=True)

    class Meta:
        model = Schedule
        fields = ('id', 'subject', 'students_assigned',
                  'professor', 'date_created')
        read_only_fields = ('id', 'date_created')


class StudentScheduleSerializer(serializers.HyperlinkedModelSerializer):
    date_joined = serializers.DateTimeField(
        format="%d-%m-%Y %I:%M%p", read_only=True)

    class Meta:
        model = Schedule
        fields = ('id', 'schedule', 'student_assigned', 'date_joined')
        read_only_fields = ('id', 'date_joined')
