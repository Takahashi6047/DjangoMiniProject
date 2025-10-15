from django.urls import path
from employees.views import dashboard

app_name = 'employees'

urlpatterns = [
    path('', dashboard.index, name='index'),
] 