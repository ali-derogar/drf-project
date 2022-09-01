from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Article
# Create your views here.

class Article_view(ListView):
    template_name = "webr/base.html"
    paginate_by = 10
    def get_queryset(self):
        return Article.objects.filter(status = True)