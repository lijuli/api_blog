from django.contrib import admin

from api.models.title import Title
from api.models.category import Category
from api.models.genre import Genre
from api.models.review import Review
from api.models.comment import Comment


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'genre')
    list_filter = ('genre',)
    empty_value_display = '-empty-'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('slug',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('slug',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'title', 'score', 'author', 'pub_date')
    search_fields = ('title',)
    list_filter = ('pub_date',)
    empty_value_display = '-empty-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'review', 'author', 'pub_date')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-empty-'
