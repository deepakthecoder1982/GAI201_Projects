from django.contrib import admin
from .models import Department, Course, Instructor, Student, Enrollment

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Enrollment)
