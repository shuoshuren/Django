from django.urls import path,re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    re_path(r'^$',views.index),
    re_path(r'^(\d+)$',views.show)
]