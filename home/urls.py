from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^announcements/$', views.announcements),
    url(r'^questions/$', views.questions),
    url(r'^discussions/$', views.discussions),
    url(r'^discussions/(?P<postTitle>[a-zA-Z0-9_\d\-_\s]+)/$', views.specificDiscussion),
    url(r'^discussions/(?P<postTitle>[a-zA-Z0-9_\d\-_\s]+)/postComment/$', views.discussionPostComment),
    url(r'^profile/', views.profile),
]