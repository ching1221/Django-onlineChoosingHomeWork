from django.db import models
# -*- coding: utf-8 -*-


# project table
class Project(models.Model):
    Name = models.CharField(max_length=100)  # 题目名称
    Desc = models.CharField(max_length=200)  # 题目描述
    MaxNum = models.IntegerField()  # 还可支持多少支队伍选择

    def __unicode__(self):
        return u'%s' % (self.Name,)


# team table
class Team(models.Model):
    SelectProject = models.ForeignKey(Project)  # 所选项目

    def __unicode__(self):
        return u'%s %s' % (self.SelectProject.Name, self.id)


# student table
class Student(models.Model):
    StuId = models.CharField(max_length=20, primary_key=True)  # 学号
    StuName = models.CharField(max_length=30)  # 姓名
    team = models.ForeignKey(Team)  # 所属队伍

    def __unicode__(self):
        return u'%s %s %s' % (self.StuId, self.StuName, self.team)
