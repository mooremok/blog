from django.shortcuts import render, redirect
from . models import Comments
from note.models import Note


def post_comments(request, note_id):
    note_detail = Note.objects.get(id=note_id)
    if request.method == "POST":
        nickname = request.POST.get("nickname", '')
        email = request.POST.get('email', '')
        content = request.POST.get('content', '')
        target = note_detail
 
        dicts = {
            'nickname': nickname,
            'email': email,
            'content': content,
            'target': target,
        }

        Comments.objects.create(**dicts)
        from note.views import note_detail
        #如果重定向到实例，那么对应的model中需要写get_absolute_url的方法
        return redirect('note_detail', note_id)
