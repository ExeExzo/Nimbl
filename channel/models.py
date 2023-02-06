from django.db import models
from user.models import Userdata

# Create your models here.

class Channeldata(models.Model):
    user = models.ForeignKey(Userdata, models.DO_NOTHING)
    subscribers = models.IntegerField(blank=True, null=True)
    videos = models.IntegerField(blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)
    comments = models.IntegerField(blank=True, null=True)
    playlists = models.IntegerField(blank=True, null=True)
    channel_level = models.IntegerField(blank=True, null=True)
    total_views = models.IntegerField(blank=True, null=True)
    followers = models.IntegerField(blank=True, null=True)
    shares = models.IntegerField(blank=True, null=True)
    total_uploads = models.IntegerField(blank=True, null=True)
    total_comments = models.IntegerField(blank=True, null=True)
    avg_views_per_video = models.FloatField(blank=True, null=True)
    avg_engagement_per_video = models.FloatField(blank=True, null=True)
    demographics = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ChannelData'
