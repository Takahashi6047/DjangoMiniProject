from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from students.models import student
from api.serializers import StudentSerializer


class StudentsList(APIView):
    def get(self, request):
        students = student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentsDetail(APIView):
    def get_object(self, pk):
        try:
            return student.objects.get(pk=pk)
        except student.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        student_obj = self.get_object(pk=pk)
        serializer = StudentSerializer(student_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        student_obj = self.get_object(pk)
        serializer = StudentSerializer(student_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        student_obj = self.get_object(pk=pk)
        student_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)