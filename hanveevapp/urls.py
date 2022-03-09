from django.http import request
from django.urls import URLPattern, path
from hanveevapp import views

urlpatterns=[
    path('',views.index),
    #abi--------------------------------------------------
    path('about/',views.about),
    # path('news/',views.about),
    path('career_view/',views.career_view),
    path('contact/',views.contact),
    path('tender_view/',views.tender_view),
    path('ga/',views.ga),
    
    #----------------------------------------------

    #vishnu-  ADMIN ----------------------------------------------
      path('homepage/', views.homepage),
    path('admin_login/', views.admin_login),
    path('admin_logout/', views.admin_logout),
    path('tender_reg/',views.tender_reg),
    path('tender_delete/',views.tender_delete),
    path('tender_update/',views.tender_update),
    path('career_reg/',views.career_reg),
    path('career_delete/',views.career_delete),
    path('career_update/',views.career_update),
    path('news/', views.news), 
    path('newsdelete/', views.newsdelete),

    #vishnu--------------------------
]