from django.contrib import admin
from .models import *
# Register your models here.

class ChanneldataAdmin(admin.ModelAdmin):
    list_display = ['user', 'subscribers', 'videos', 'likes', 'comments', 'playlists','channel_level', 'total_views', 'followers', 'shares', 'total_uploads', 'total_comments', 'avg_views_per_video', 'avg_engagement_per_video', 'demographics']
    list_display_links = ('user', 'subscribers', 'videos')
    search_fields =('user', 'subscribers', 'videos')

admin.site.register(Channeldata, ChanneldataAdmin)