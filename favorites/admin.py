from django.contrib import admin
from . models import Favorites
# Register your models here.

@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    list_display = ['title', 'desc', 'the_url', 'created_time']