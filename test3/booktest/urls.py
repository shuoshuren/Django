from django.urls import path,include,re_path

from . import views

urlpatterns = [
    # re_path(r'^$', views.index),
    path('',views.index),
    re_path(r'^(\d+)$',views.detail),
    re_path(r'^getTest1$',views.getTest1),
    re_path(r'^getTest2$',views.getTest2),
    re_path(r'^getTest3$',views.getTest3),
    re_path(r'^postTest1$',views.postTest1),
    re_path(r'^postTest2$',views.postTest2),
    re_path(r'^(?P<month>\d+)/(?P<year>\d+)/(?P<day>\d+)/$',views.detail)
]