from django.contrib import admin
from .models import Post


class PostList(admin.ModelAdmin):
    list_display = ('name', 'year', 'body', 'rating')
    list_filter = ('name', 'year', 'rating')
    search_fields = ('name', 'description')
    ordering = ['year']


admin.site.register(Post, PostList)
