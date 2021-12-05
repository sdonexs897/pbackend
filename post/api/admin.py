from django.contrib import admin
from .models import Post


class PostList(admin.ModelAdmin):
    list_display = ('name', 'year', 'body')
    list_filter = ('name', 'year', )
    search_fields = ('name', 'body')
    ordering = ['year']


admin.site.register(Post, PostList)
