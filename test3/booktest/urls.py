from django.urls import path,include,re_path

from . import views

urlpatterns = [
    # re_path(r'^$', views.index),
    path('',views.index),
    re_path(r'^(\d+)$',views.detail),
    re_path(r'^(?P<month>\d+)/(?P<year>\d+)/(?P<day>\d+)/$',views.detail)
]