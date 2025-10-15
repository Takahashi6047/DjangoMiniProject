from django.urls import path
from api.views import student_function_based_view, employee_function_based_view

urlpatterns = [
    path('fbw_students/', student_function_based_view.studentsList),
    path('fbw_students/<int:pk>/', student_function_based_view.studentDetailView),

    path('fbw_employees/', employee_function_based_view.employeesList),
    path('fbw_employees/<int:pk>/', employee_function_based_view.employeeDetailView),
]