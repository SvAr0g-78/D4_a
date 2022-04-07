from django.contrib import admin
from .models import Author, Category, Post, Comment  # D3


# Define the admin class

class AuthorAdmin(admin.ModelAdmin):
    list_ = ('id', 'rating_author', 'name')


# Register the admin class with the associated model

admin.site.register(Author, AuthorAdmin)

# admin.site.register(Author, Category, Post, PostCategory, Comment)

# Register the Admin classes for Post using the decorator


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('dateCreation', 'author', 'title', 'text', 'rating')


# Register the Admin classes for Comment using the decorator

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('dateCreation', 'commentUser_id', 'rating', 'text', 'commentPost_id')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')