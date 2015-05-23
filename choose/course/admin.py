from django.contrib import admin
# Register your models here.


from course.models import Student, Team, Project

admin.site.register(Student)
admin.site.register(Team)
admin.site.register(Project)
