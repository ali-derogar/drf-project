from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from webr.models import Article
from django.contrib.auth.models import User

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        # fields = ['title','slug','content','author','status','published','created','updated']
        # exclude = ['created','updated']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__s"