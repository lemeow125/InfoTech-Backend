from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics
from .serializers import SubjectSerializer
from .models import Subject


class SubjectViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all().order_by('-year_level')


class FirstYearSubjectViewSet(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = SubjectSerializer
    queryset = Subject.objects.filter(year_level='1st Year')


class SecondYearSubjectViewSet(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = SubjectSerializer
    queryset = Subject.objects.filter(year_level='2nd Year')


class ThirdYearSubjectViewSet(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = SubjectSerializer
    queryset = Subject.objects.filter(year_level='3rd Year')


class FourthYearSubjectViewSet(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = SubjectSerializer
    queryset = Subject.objects.filter(year_level='4th Year')
