from django.db import models
from user.models import Userdata

# Create your models here.

class Categories(models.Model):
    category_id = models.AutoField(db_column='Category_id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.
    parent_id = models.IntegerField(db_column='Parent_id')  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='Created_at')  # Field name made lowercase.
    updated_at = models.DateTimeField(db_column='Updated_at')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Categories'


class Playlists(models.Model):
    playlist_id = models.AutoField(db_column='Playlist_id', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('user.Userdata', models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    playlist_name = models.CharField(db_column='Playlist_name', max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='Created_at')  # Field name made lowercase.
    updated_at = models.DateTimeField(db_column='Updated_at')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Playlists'


class Videoanalytics(models.Model):
    video = models.ForeignKey('video.Videodetails', models.DO_NOTHING)
    watch_time = models.TimeField(blank=True, null=True)
    ctr = models.FloatField(blank=True, null=True)
    avg_view_length = models.TimeField(blank=True, null=True)
    drop_off_rate = models.FloatField(blank=True, null=True)
    audience_retention = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VideoAnalytics'


class Videodetails(models.Model):
    video_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    video_file = models.CharField(max_length=255, blank=True, null=True)
    uploader = models.ForeignKey('user.Userdata', models.DO_NOTHING, db_column='uploader')
    duration = models.TimeField(blank=True, null=True)
    views = models.IntegerField(blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)
    fun_tokens = models.IntegerField(blank=True, null=True)
    value_tokens = models.IntegerField(blank=True, null=True)
    comments = models.IntegerField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    upload_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(Categories, models.DO_NOTHING, db_column='category')
    privacy = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VideoDetails'


class Viewerinformation(models.Model):
    user = models.ForeignKey(Userdata, models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    video = models.ForeignKey(Videodetails, models.DO_NOTHING)
    geo_location = models.CharField(max_length=255, blank=True, null=True)
    device = models.CharField(max_length=255, blank=True, null=True)
    referrer = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ViewerInformation'


class Views(models.Model):
    view_id = models.AutoField(db_column='View_id', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey(Userdata, models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    video = models.ForeignKey(Videodetails, models.DO_NOTHING, db_column='Video_id',related_name="video1")  # Field name made lowercase.
    view_time = models.DateTimeField(db_column='View_time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Views'