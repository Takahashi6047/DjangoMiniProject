from django.shortcuts import render
from students.models import student
from ..serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET'])
def studentsList(request):
    if request.method == 'GET':
        students = student.objects.all()
        serialize = StudentSerializer(students, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)