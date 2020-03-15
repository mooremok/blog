from django.contrib import admin
from . models import Note, Category

# Register your models here.
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'cover', 'created_time']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']