__author__ = 'qing'
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
# 导入数据库信息
from course.models import Student, Team, Project
# 解决编码错误
import sys
reload(sys)
sys.setdefaultencoding("utf8")


# 记录选题
def collect(request):
    if request.POST['stuid1'] or request.POST['stuid2'] or request.POST['stuid3']:
        if request.POST['projectid']:
            # 题目所选队伍上限判断
            SelectP = Project.objects.get(id=int(request.POST['projectid']))
            if SelectP.MaxNum is 0:
                return HttpResponse("题目所选人数达到上限，请重选"+"<br/>"+"<a href=\"course/ \">返回选题</a>")
            # 创建队伍
            newt = Team.objects.create(SelectProject=SelectP)
            if request.POST['stuid1'] and request.POST['stuname1']:
                stuid1 = request.POST['stuid1']
                stuname1 = request.POST['stuname1']
                try:
                    Student.objects.get(StuId=stuid1)
                except Student.DoesNotExist:
                    temp1 = Student.objects.create(StuId=stuid1, StuName=stuname1, team=newt)
                else:
                    # 出错则删除
                    newt.delete()
                    return HttpResponse("人员已经录入过，请仔细核对！"+"<br/>"+"<a href=\"course/ \">返回选题</a>")
            if request.POST['stuid2'] and request.POST['stuname2']:
                stuid2 = request.POST['stuid2']
                stuname2 = request.POST['stuname2']
                try:
                    Student.objects.get(StuId=stuid2)
                except Student.DoesNotExist:
                    temp2 = Student.objects.create(StuId=stuid2, StuName=stuname2, team=newt)
                else:
                    # 出错则删除
                    newt.delete()
                    temp1.delete()
                    return HttpResponse("人员已经录入过，请仔细核对！"+"<br/>"+"<a href=\"course/ \">返回选题</a>")
            if request.POST['stuid3'] and request.POST['stuname3']:
                stuid3 = request.POST['stuid3']
                stuname3 = request.POST['stuname3']
                try:
                    Student.objects.get(StuId=stuid3)
                except Student.DoesNotExist:
                    Student.objects.create(StuId=stuid3, StuName=stuname3, team=newt)
                else:
                    # 出错则删除
                    newt.delete()
                    temp1.delete()
                    temp2.delete()
                    return HttpResponse("人员已经录入过，请仔细核对！"+"<br/>"+"<a href=\"course/ \">返回选题</a>")
            # 题目可供选择的数目减1
            SelectP.MaxNum -= 1
            SelectP.save()
            return HttpResponse("选题成功，请查询核对！"+"<br/>"+"<a href=\"/query/ \">去查询</a>")
        else:
            return HttpResponse("输入错误，请仔细核对！"+"<br/>"+"<a href=\"course/ \">返回选题</a>")


# 首页显示选题
def homepage(request):
    temp = get_template("course/index.html")
    Pro_List = Project.objects.all()
    return HttpResponse(temp.render({'Pros': Pro_List, 'Desc1': Pro_List[0].Desc, 'Remain1': Pro_List[0].MaxNum}))


# 查询个人选题情况
def query(request):
    temp = get_template("course/query.html")
    if 'stuid' in request.POST:
        try:
            p = Student.objects.get(StuId=request.POST['stuid'])
        except Student.DoesNotExist:
            pro_name = "您还没有登记过选题情况哦～"
        else:
            pro_name = p.StuName + "，您好，您的选题是" + p.team.SelectProject.Name
        ct = Context({'result': pro_name})
        return HttpResponse(temp.render(ct))
    else:
        return HttpResponse(temp.render())


# 获取题目要求
def desc(request):
    if 'proid' in request.GET:
        proid = request.GET['proid']
        tempp = Project.objects.get(id=proid)
        return HttpResponse(tempp.Desc+"###"+str(tempp.MaxNum))
    else:
        return HttpResponse("参数错误！")