from django.urls import path
from api.views import student_function_based_view

urlpatterns = [
    path('fbw_students/', student_function_based_view.studentsList)
]