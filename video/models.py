from django.db import models
from user.models import Userdata
# Create your models here.

class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    parent_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'categories'


class Playlists(models.Model):
    playlist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Userdata, models.DO_NOTHING)
    playlist_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'playlists'


class Videoanalytics(models.Model):
    video = models.ForeignKey('Videodetails', models.DO_NOTHING , related_name='video+')
    watch_time = models.TimeField(blank=True, null=True)
    ctr = models.FloatField(blank=True, null=True)
    avg_view_length = models.TimeField(blank=True, null=True)
    drop_off_rate = models.FloatField(blank=True, null=True)
    audience_retention = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'videoanalytics'


class Videodetails(models.Model):
    video_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    video_file = models.CharField(max_length=255, blank=True, null=True)
    uploader = models.ForeignKey(Userdata, models.DO_NOTHING, db_column='uploader')
    duration = models.DurationField(blank=True, null=True)
    views = models.IntegerField(blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)
    fun_tokens = models.IntegerField(blank=True, null=True)
    value_tokens = models.IntegerField(blank=True, null=True)
    comments = models.IntegerField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    upload_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(Categories, models.DO_NOTHING, db_column='category')
    privacy = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'videodetails'


class Viewerinformation(models.Model):
    user = models.ForeignKey(Userdata, models.DO_NOTHING)
    video = models.ForeignKey('Videodetails', models.DO_NOTHING, related_name='video+')
    geo_location = models.CharField(max_length=255, blank=True, null=True)
    device = models.CharField(max_length=255, blank=True, null=True)
    referrer = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'viewerinformation'


class Views(models.Model):
    view_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Userdata, models.DO_NOTHING)
    video = models.ForeignKey('Videodetails', models.DO_NOTHING, related_name='video+')
    view_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'views'
