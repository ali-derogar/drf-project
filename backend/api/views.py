from .serializers import ArticleSerializer
from webr.models import Article
from rest_framework.generics import ListAPIView , ListCreateAPIView


class Artilelist(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
