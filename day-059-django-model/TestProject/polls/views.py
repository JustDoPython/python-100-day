from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from polls.models import Choice, Question
from django.utils import timezone

def index(request):
    return HttpResponse("你好，这是一个投票页面。")

def add(request):
    question = Question(question_text='双十一你在哪个平台剁手？',pub_date=timezone.now())
    question.save();
    return HttpResponse("新增投票成功！")    

def query(request):
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM question
    questionList = Question.objects.all()
    # 获取单个对象
    response2 = Question.objects.get(id=1) 
    # 相当于SQL中的WHERE id=1，可设置条件过滤
    response3 = Question.objects.filter(id=1) 
    #根据id字段排序
    response5 = Question.objects.order_by("id")    

    res = ""
    # 遍历所有对象
    for q in questionList:
        res += str(q.id) + "." + q.question_text + " <br />" 
    return HttpResponse("查询所有问题：<br />" + res)

def update(request):
    question1 = Question.objects.get(id=1)
    question1.question_text = '天猫和京东你会选哪个？'
    question1.save()

    # 通过条件过滤的方式也可以更新一条或多条数据
    # Question.objects.filter(id=1).update(question_text='天猫和京东你会选哪个？')

    return HttpResponse("更新id=1：" + question1.question_text)

def delete(request):
    question2 = Question.objects.get(id=2)
    question2.delete()

    # 通过条件过滤的方式也可以删除一条或多条数据
    # Question.objects.filter(id=2).delete()
    
    # 删除所有数据
    # Question.objects.all().delete()
    
    res3 = ''
    questionList = Question.objects.all()
    # 遍历所有对象
    for q in questionList:
        res3 += str(q.id) + "." + q.question_text + " <br />"
    return HttpResponse("删除后查询：<br />" + res3)
