from django.db import models

# Create your models here.

class Favorites(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    desc = models.TextField(verbose_name='简介')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='收藏时间')
    the_url = models.URLField(verbose_name='连接')

    def __str__(self):
        return self.the_url
    
    class Meta:
        ordering = ['-created_time']
    
    @classmethod
    def get_all_favorites(cls):
        return cls.objects.all()
