# -*- coding: utf-8 -*-

from django.contrib import admin
# Register your models here.
# 解决编码错误
import sys
reload(sys)
sys.setdefaultencoding("utf8")
from course.models import Student, Team, Project


class StudentAdmin(admin.ModelAdmin):
    list_display = ('StuId', 'StuName', 'team',)
    list_filter = ('team',)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('SelectProject',)
    list_filter = ('SelectProject',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Desc', 'MaxNum')

admin.site.register(Student, StudentAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Project, ProjectAdmin)
