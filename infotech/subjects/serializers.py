from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Subject
from students.models import Student


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    students = serializers.SlugRelatedField(
        queryset=Student.objects.all(), many=True, slug_field='full_name', allow_null=True)

    class Meta:
        model = Subject
        fields = ('id', 'name', 'students',
                  'max_slots', 'year_level', 'semester')
        read_only_fields = ('id',)
