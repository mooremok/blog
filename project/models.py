from django.db import models
from mdeditor.fields import MDTextField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name='主题')
    desc = models.TextField(max_length=100, verbose_name='说明')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    content = MDTextField(verbose_name='文章内容')
    cover = models.ImageField(upload_to='project_cover', help_text='190*230')

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_time'] 
    
    @classmethod
    def get_all_obj(cls):
        return cls.objects.all()
    
    @staticmethod
    def get_project_detail(p_id):
        return Project.objects.get(id=p_id)