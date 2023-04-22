from rest_framework import viewsets, generics
from .models import TimeSlot, TimeSchedule
from .serializers import TimeScheduleSerializer, TimeSlotSerializer

# Create your views here.


class TimeSlotViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = TimeSlotSerializer
    queryset = TimeSlot.objects.all()


class TimeScheduleViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = TimeScheduleSerializer
    queryset = TimeSchedule.objects.all()
