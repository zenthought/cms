from django.conf.urls import url
from web import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^technology_blog.html', views.technology_blog),

]
