from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics
from .serializers import ScheduleSerializer
from .models import Schedule, StudentSchedule


class ScheduleViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()


class FirstYearScheduleViewSet(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.filter(year_level='1st Year')


class SecondYearScheduleViewSet(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.filter(year_level='2nd Year')


class ThirdYearScheduleViewSet(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.filter(year_level='3rd Year')


class FourthYearScheduleViewSet(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.filter(year_level='4th Year')
