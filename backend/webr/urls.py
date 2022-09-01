from django.urls import path , include
from .views import Article_view

app_name = "webr"
urlpatterns = [
    path('',Article_view.as_view(),name="home")
]