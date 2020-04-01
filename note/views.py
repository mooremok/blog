from django.shortcuts import render
from . models import Note, Category
from django.core.paginator import Paginator
#使用markdown，将markdown格式渲染成html格式
import markdown
# Create your views here.

def note_detail(request, note_id):
    content = Note.objects.get(id=note_id)
    content.increase_views()
    content.content = markdown.markdown(content.content,
                        extensions = [
                            'markdown.extensions.extra',
                            'markdown.extensions.codehilite',
                            'markdown.extensions.toc',
                    ])
    categories = Category.get_all_categories()
    comments_count = content.comments_set.count()
    context = {
        'content': content,
        'categories': categories,
        'comments_count': comments_count,
    }
    return render(request, 'note/detail.html', context)

def category_list(request, cate_id):
    notes = Category.objects.get(id=cate_id).note_set.all().order_by('-id')
    paginator = Paginator(notes, 20)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    categories = Category.get_all_categories()
    context = {
        'paginator': paginator,
        'page_obj': page_obj,
        'is_paginated': True,
        'categories': categories,

    }
    return render(request, 'note/list.html', context)
    
