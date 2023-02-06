from django.contrib import admin
from .models import *
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_id', 'user', 'video', 'comment_text', 'comment_time', 'parent_comment_id']
    list_display_links = ('comment_id', 'user')
    search_fields =('comment_id', 'user', 'video', 'comment_text', 'comment_time')

class DislikesAdmin(admin.ModelAdmin):
    list_display = ['dislike_id', 'user', 'video', 'dislike_time']
    list_display_links = ('dislike_id', 'user', 'video', 'dislike_time')
    search_fields =('dislike_id', 'user', 'video', 'dislike_time')

class LikesAdmin(admin.ModelAdmin):
    list_display = ['like_id', 'user', 'video', 'like_time']
    list_display_links = ('like_id', 'user', 'video', 'like_time')
    search_fields =('like_id', 'user', 'video', 'like_time')

admin.site.register(Comment, CommentAdmin)
admin.site.register(Dislikes, DislikesAdmin)
admin.site.register(Likes, LikesAdmin)