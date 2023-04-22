from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import ScheduleSerializer
from .models import Schedule


class ScheduleViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()
