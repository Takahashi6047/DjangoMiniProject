from django.urls import path
from .views import dashboard

app_name = 'employees'

urlpatterns = [
    path('', dashboard.index, name='index'),
] 