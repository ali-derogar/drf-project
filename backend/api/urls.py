from django.urls import path , include
from .views import Artilelist

app_name = "api"
urlpatterns = [
    path('',Artilelist.as_view(),name="home")
]