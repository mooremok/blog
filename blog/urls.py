"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from note.views import handler, show
from django.conf.urls.static import static
from django.conf import settings
from home.views import index, MySearchView
from note.views import note_detail, category_list
from project.views import project_list, project_detail
import haystack
from home.views import get_logs
from favorites.views import show_favorites
from comments.views import post_comments

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('mdeditor/', include('mdeditor.urls')),
    path('', index, name='index'),
    path('note-detail/<note_id>', note_detail, name='note_detail'),
    path('category/<cate_id>', category_list, name='category_list'),
    path('projects/', project_list, name='project_list'),
    path('projects/detail/<p_id>', project_detail, name='project_detail'),
    path('search/', MySearchView(), name='haystack_search'),
    path('logs/', get_logs, name='logs'),
    path('favorites/', show_favorites, name='favorites'),
    path('comments/<int:note_id>', post_comments, name='comments')
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
