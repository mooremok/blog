from django.shortcuts import render
from note.models import Note, Category
from django.core.paginator import Paginator #分页器
from . models import BlogLog

from haystack.views import SearchView

def index(request):
    notes = Note.get_all_notes()
    categories = Category.get_all_categories()
    paginator = Paginator(notes, 20)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {
        'page_obj': page_obj,
        'paginator': paginator,
        'is_paginated': True,
        'categories': categories,
    }
    return render(request, 'home/index.html', context)

class MySearchView(SearchView):
    """重写extra_content方法，把导航的分类加进入，不然搜索结果的页面没有导航"""
    def extra_context(self):
        categories = Category.get_all_categories()
        context = {
            'categories': categories,
        }
        return context

def get_logs(request):
    logs = BlogLog.get_all_logs()
    categories = Category.get_all_categories()
    context = {
        'logs': logs,
        'categories': categories,
    }
    return render(request, 'home/bloglog.html', context)