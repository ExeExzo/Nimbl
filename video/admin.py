from django.contrib import admin
from .models import *
# Register your models here.

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['category_id', 'name', 'description', 'parent_id', 'created_at', 'updated_at']
    list_display_links = ('category_id', 'name', 'description', 'parent_id', 'created_at', 'updated_at')
    search_fields =('category_id', 'name', 'description', 'parent_id', 'created_at', 'updated_at')

class PlaylistsAdmin(admin.ModelAdmin):
    list_display = ['playlist_id', 'user', 'playlist_name', 'description', 'created_at', 'updated_at']
    list_display_links = ('playlist_id', 'user', 'playlist_name', 'description', 'created_at', 'updated_at')
    search_fields =('playlist_id', 'user', 'playlist_name', 'description', 'created_at', 'updated_at')

class VideoanalyticsAdmin(admin.ModelAdmin):
    list_display = ['video', 'watch_time', 'ctr', 'avg_view_length', 'drop_off_rate', 'audience_retention']
    list_display_links = ('video', 'watch_time', 'ctr', 'avg_view_length', 'drop_off_rate', 'audience_retention')
    search_fields =('video', 'watch_time', 'ctr', 'avg_view_length', 'drop_off_rate', 'audience_retention')

admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Playlists, PlaylistsAdmin)
admin.site.register(Videoanalytics, VideoanalyticsAdmin)
