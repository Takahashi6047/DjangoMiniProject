from rest_framework import generics
from employees.models import Employee
from api.serializers import EmployeeSerializer

class EmployeesList(generics.ListCreateAPIView, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeesDetail(generics.RetrieveUpdateDestroyAPIView, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'