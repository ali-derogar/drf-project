from rest_framework import serializers
from webr.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        # fields = ['title','slug','content','author','status','published','created','updated']
        # exclude = ['created','updated']
