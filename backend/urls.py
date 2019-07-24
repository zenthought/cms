from django.conf.urls import url
from backend import views

urlpatterns = [

    url(r'^article_list/', views.article_list, name='article_list'),
    url(r'^article_add/', views.article_add, name='article_add'),
    url(r'^article_edit/(\d+)/', views.article_edit, name='article_edit'),
    url(r'^article_del/(\d+)/', views.article_del, name='article_del'),

]
