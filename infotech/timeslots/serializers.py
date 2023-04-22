from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TimeSlot, TimeSchedule


class TimeSlotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TimeSlot
        fields = ('id', 'name', 'time_start', 'time_end')
        read_only_fields = ['id', 'name']


class TimeScheduleSerializer(serializers.HyperlinkedModelSerializer):
    time_window = serializers.SlugRelatedField(
        queryset=TimeSlot.objects.all(), slug_field='name')

    class Meta:
        model = TimeSchedule
        fields = ('id', 'name', 'day', 'time_window')
        read_only_fields = ['id', 'name']
