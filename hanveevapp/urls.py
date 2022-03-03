from django.http import request
from django.urls import URLPattern, path
from hanveevapp import views

urlpatterns=[
    path('',views.index),
    path('admin-login/',views.adminlogin)

]
