from django.urls import path
from api.views import student_function_based_view, employee_function_based_view, student_class_based_view, employee_class_based_view


urlpatterns = [
    path('fbw_students/', student_function_based_view.studentsList),
    path('fbw_students/<int:pk>/', student_function_based_view.studentDetailView),

    path('fbw_employees/', employee_function_based_view.employeesList),
    path('fbw_employees/<int:pk>/', employee_function_based_view.employeeDetailView),

    path('cbv_students/', student_class_based_view.StudentsList.as_view(), name='students-list'),
    path('cbv_students_detail/<int:pk>/', student_class_based_view.StudentsDetail.as_view(), name='students-detail'),

    path('cbv_employees/', employee_class_based_view.EmployeesList.as_view(), name='employees-list'),
    path('cbv_employees_detail/<int:pk>/', employee_class_based_view.EmployeesDetail.as_view(), name='employees-detail'),
]