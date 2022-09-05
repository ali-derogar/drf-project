from django.shortcuts import render , get_object_or_404
from .serializers import ArticleSerializer , UserSerializer
from webr.models import Article
from django.contrib.auth.models import User
from rest_framework.generics import (ListAPIView ,
                                        ListCreateAPIView ,
                                        RetrieveAPIView ,
                                        DestroyAPIView , 
                                        RetrieveDestroyAPIView , 
                                        UpdateAPIView , 
                                        RetrieveUpdateAPIView ,
                                        RetrieveUpdateDestroyAPIView
                                        )


class Articlelist(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
class Articledetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "slug"

class Userlist(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class Userdetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
