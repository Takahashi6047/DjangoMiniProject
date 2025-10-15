from django.contrib import admin
from .models import Employee

# Register your models here.
# @admin.register(Employee)
# # class EmployeeAdmin(admin.ModelAdmin):
# #     list_display = ('emp_id', 'emp_name', 'designation')
# #     search_fields = ('emp_id', 'emp_name', 'designation')


admin.site.register(Employee)