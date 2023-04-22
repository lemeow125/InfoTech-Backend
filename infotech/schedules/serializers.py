from rest_framework import serializers
from .models import Schedule


class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    date_created = serializers.DateTimeField(
        format="%d-%m-%Y %I:%M%p", read_only=True)

    class Meta:
        model = Schedule
        fields = ('id', 'subject', 'students_assigned',
                  'professor', 'date_created')
        read_only_fields = ('id', 'date_created')
