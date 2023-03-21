from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('subjects.urls')),
    path('', include('students.urls')),
    path('accounts/', include('accounts.urls')),
]
