from django.shortcuts import render
from students.models import student


def studentsView(request):
    students = student.objects.all()