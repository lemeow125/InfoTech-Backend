from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student
from subjects.models import Subject


class StudentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'middle_name', 'last_name',
                  'age', 'sex', 'birthdate',
                  'address', 'birthplace',
                  'mother_name', 'father_name',
                  'registrar_done', 'clearance_done', 'pta_done',
                  'year_level', 'current_semester'
                  ]
        read_only_fields = ['id']
