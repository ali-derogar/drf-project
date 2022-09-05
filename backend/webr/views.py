from django.shortcuts import get_object_or_404 , render
from django.views.generic import ListView , DetailView
from .models import Article
from django.contrib.auth.models import User
# Create your views here.

class Articlelist(ListView):
    template_name = "webr/list.html"
    paginate_by = 10
    def get_queryset(self):
        return Article.objects.filter(status = True)
    
class Articledetail(DetailView):
    template_name = "webr/detail.html"
    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Article , pk = pk)
    
    
class Userlist(ListView):
    template_name = "webr/user_list.html"
    paginate_by = 10
    def get_queryset(self):
        return User.objects.all()
    
class Userdetail(DetailView):
    template_name = "webr/user_detail.html"
    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(User , pk = pk)