from django.shortcuts import render
from .models import Favorites
from note.models import Category
# Create your views here.

def show_favorites(request):
    favorites = Favorites.get_all_favorites()
    categories = Category.get_all_categories()
    context = {
        'favorites': favorites,
        'categories': categories,
    }
    return render(request, 'favorites/list.html', context)
