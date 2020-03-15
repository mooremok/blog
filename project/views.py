from django.shortcuts import render
from .models import Project
from note.models import Category
import markdown
# Create your views here.

def project_list(request):
    projects = Project.get_all_obj()
    categories = Category.get_all_categories()
    context = {
        'categories': categories,
        'projects': projects,
    }
    return render(request, 'project/list.html', context)

def project_detail(request, p_id):
    content = Project.get_project_detail(p_id)
    categories = Category.get_all_categories()
    content.content = markdown.markdown(content.content,
                        extensions = [
                            'markdown.extensions.extra',
                            'markdown.extensions.codehilite',
                            'markdown.extensions.toc',
                    ])
    categories = Category.get_all_categories()
    context = {
        'content': content,
        'categories': categories,
    }
    return render(request, 'project/detail.html', context)
