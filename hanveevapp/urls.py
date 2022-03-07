from django.http import request
from django.urls import URLPattern, path
from hanveevapp import views

urlpatterns=[
    path('',views.index),
    #abi--------------------------------------------------
    path('about/',views.about),
    path('news/',views.about),
    path('career_reg/',views.career_reg),
    path('contact/',views.contact),
    path('tender/',views.tender),
    path('ga/',views.ga),
    
    #----------------------------------------------

    #vishnu-  ADMIN ----------------------------------------------
      path('homepage/', views.homepage),
    path('admin_login/', views.admin_login),
    path('admin_logout/', views.admin_logout),
    path('brands/', views.brands),
    path('user/', views.user),
    path('category/', views.category),
    path('products/', views.products),
    path('gallery/', views.gallery),
    path('contactus/', views.contactus),
    path('getprice/', views.getprice),
    path('newsletter/',views.newsletter),

    #vishnu--------------------------
]