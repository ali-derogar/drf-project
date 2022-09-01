from tabnanny import verbose
from venv import create
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان")
    slug = models.SlugField(max_length=50, unique=True,verbose_name="لینک")
    content = models.TextField(verbose_name="محتوا")
    author = models.ForeignKey(User,on_delete=models.CASCADE , verbose_name="نویسنده")
    status = models.BooleanField(default=True,verbose_name="وضعیت")
    published = models.DateTimeField(default=timezone.now,verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True,verbose_name="زمان ایجاد")
    updated = models.DateTimeField(auto_now=True,verbose_name="زمان بروزرسانی")
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"