from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'subjects', views.SubjectViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('first_year_subjects/', views.FirstYearSubjectViewSet.as_view()),
    path('second_year_subjects/', views.SecondYearSubjectViewSet.as_view()),
    path('third_year_subjects/', views.ThirdYearSubjectViewSet.as_view()),
    path('fourth_year_subjects/', views.FourthYearSubjectViewSet.as_view()),
]
