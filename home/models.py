from django.db import models

# Create your models here.

class BlogLog(models.Model):
    content = models.TextField(verbose_name='日志内容')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='日期')

    def __str__(self):
        return self.content
    
    class Meta:
        ordering = ['-created_time']
    
    @classmethod
    def get_all_logs(cls):
        return cls.objects.all()