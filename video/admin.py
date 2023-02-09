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

class VideodetailsAdmin(admin.ModelAdmin):
    list_display = ['video_id', 'title', 'description', 'thumbnail', 'video_file', 'uploader','duration', 'views', 'likes', 'fun_tokens', 'value_tokens', 'comments', 'tags', 'upload_date', 'category', 'privacy']
    list_display_links = ('video_id', 'title', 'description')
    search_fields =('video_id', 'title', 'description')

class ViewerinformationAdmin(admin.ModelAdmin):
    list_display = ['user', 'video', 'geo_location', 'device', 'referrer']
    list_display_links = ('user', 'video', 'geo_location')
    search_fields =('user', 'video', 'geo_location')

class ViewsAdmin(admin.ModelAdmin):
    list_display = ['view_id', 'user', 'video', 'view_time']
    list_display_links = ('view_id', 'user', 'video', 'view_time')
    search_fields =('view_id', 'user', 'video', 'view_time')

admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Playlists, PlaylistsAdmin)
admin.site.register(Videoanalytics, VideoanalyticsAdmin)
admin.site.register(Videodetails, VideodetailsAdmin)
admin.site.register(Viewerinformation, ViewerinformationAdmin)
admin.site.register(Views, ViewsAdmin)
