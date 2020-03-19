from django.contrib import admin
from home.models import BlogLog
# Register your models here.
@admin.register(BlogLog)
class BlogLogAdmin(admin.ModelAdmin):
    list_display = ['content', 'created_time']