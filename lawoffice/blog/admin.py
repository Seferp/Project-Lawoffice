from django.contrib import admin
from .models import Post, Comment


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_filter = ('date',)
    prepopulated_fields = {
        'slug': ('title',)
    }

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'post')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

