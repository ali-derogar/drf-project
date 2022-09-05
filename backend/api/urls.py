from django.urls import path , include
from .views import Articlelist , Articledetail , Userlist , Userdetail

app_name = "api"
urlpatterns = [
    path('',Articlelist.as_view(),name="home"),
    path('<slug:slug>',Articledetail.as_view(),name="detail"),
    path('users',Userlist.as_view(),name="user_home"),
    path('users/<int:pk>/',Userdetail.as_view(),name="user_detail"),
]