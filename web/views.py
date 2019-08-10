from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html')


def technology_blog(request):
    return render(request, 'technology-blog/blog.html')


def feedback_list(request, table=None):
    feedback_dict = {
        'learning-notes': {'banner': 'images/classmate-say/classmate-banner1.jpg', 'title': '学习笔记'},
        'student-evaluation': {'banner': 'images/classmate-say/classmate-banner2.jpg', 'title': '学员评价'},
        'work-invitation': {'banner': 'images/classmate-say/classmate-banner3.jpg', 'title': '入职邀约'},
    }
    return render(request, 'classmate-say/feedback.html',
                  {'table': table,
                   'banner': feedback_dict[table]['banner'],
                   'title': feedback_dict[table]['title'],
                   })


from rest_framework import generics

from repository import models
from web.serializers import FeedbackSerializer
from web.pagination import DefaultPagination
from django_filters.rest_framework import DjangoFilterBackend


class AjaxFeedback(generics.ListAPIView, ):
    queryset = models.Feedback.objects.all()
    serializer_class = FeedbackSerializer   #序列化
    pagination_class = DefaultPagination  #分页
    filter_backends = [DjangoFilterBackend,]  #
    filter_fields = ['back_type']  #过滤器
