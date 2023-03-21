from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Subject


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    enrolled_count = serializers.IntegerField(required=False, default=0)

    class Meta:
        model = Subject
        fields = ('id', 'name', 'enrolled_count', 'max_slots', 'year_level')
        read_only_fields = ('id',)
