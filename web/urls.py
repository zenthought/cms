from django.conf.urls import url
from web import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^technology_blog.html', views.technology_blog),
    url(r'^(student-evaluation|learning-notes|work-invitation)\.html', views.feedback_list,name='feedback'),
    url(r'^ajax_feedback', views.AjaxFeedback.as_view()),

]
