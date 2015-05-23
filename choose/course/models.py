from django.db import models
# -*- coding: utf-8 -*-


# project table
class Project(models.Model):
    Name = models.CharField(max_length=100)
    Desc = models.CharField(max_length=200)
    MaxNum = models.IntegerField()  # 还可支持多少支队伍选择

    def __unicode__(self):
        return u'%s %s %s %s' % (self.id, self.Name, self.Desc, self.MaxNum)


# team table
class Team(models.Model):
    SelectProject = models.ForeignKey(Project)

    def __unicode__(self):
        return u'%s %s' % (self.SelectProject.Name, self.id)


# student table
class Student(models.Model):
    StuId = models.CharField(max_length=20, primary_key=True)
    StuName = models.CharField(max_length=30)
    team = models.ForeignKey(Team)

    def __unicode__(self):
        return u'%s %s %s' % (self.StuId, self.StuName, self.team)
