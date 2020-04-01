from django import template
from comments.models import Comments

register = template.Library()

@register.inclusion_tag('comments/inclusions/comment_content.html', takes_context=True)
def show_comments(context, content):
    comment_list = content.comments_set.all()
    comment_count = comment_list.count()
    comment_context = {
        'comment_list': comment_list,
        'comment_count': comment_count,
    }
    return comment_context

@register.inclusion_tag('comments/inclusions/comment_post.html', takes_context=True)
def comments_post(context, content):
    return {
        'content': content,
    }