from django.contrib import admin

# Register your models here.

from app.models import employee

class employee_admin(admin.ModelAdmin):
    list_display=['emp_id','emp_name','emp_dept','emp_mobile','emp_salary']
    ordering=['emp_id']

admin.site.register(employee,employee_admin)
