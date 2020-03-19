from django.db import models
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField
# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=20, verbose_name="分类")

    def __str__(self):
        return self.category
    
    @classmethod
    def get_all_categories(cls):
        return cls.objects.all()

class Note(models.Model):
    author = models.ForeignKey(User, verbose_name="作者", on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name="分类")
    title = models.CharField(max_length=500, verbose_name="标题")
    desc = models.TextField(max_length=500, verbose_name="摘要", null=True, blank=True)
    content = MDTextField(verbose_name='文章内容')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    cover = models.ImageField(upload_to='cover', help_text='160*100')
    views = models.PositiveIntegerField(default=0, editable=True, verbose_name='阅读量')

    def __str__(self):
        return self.title
    
    #使用类方法获取所有文章，遵循数据操作尽量封装在model中的原则
    @classmethod
    def get_all_notes(cls):        
        return cls.objects.all().order_by('-id')
    
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])