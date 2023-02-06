from django.db import models
from user.models import Userdata
from video.models import Videoanalytics, Videodetails

# Create your models here.

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('user.Userdata', models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    video = models.ForeignKey('video.Videodetails', models.DO_NOTHING, db_column='Video_id')  # Field name made lowercase.
    comment_text = models.TextField(db_column='Comment_text')  # Field name made lowercase.
    comment_time = models.DateTimeField(db_column='Comment_time')  # Field name made lowercase.
    parent_comment_id = models.IntegerField(db_column='Parent_comment_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Comment'

class Dislikes(models.Model):
    dislike_id = models.AutoField(db_column='Dislike_id', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('user.Userdata', models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    video = models.ForeignKey('video.Videodetails', models.DO_NOTHING, db_column='Video_id')  # Field name made lowercase.
    dislike_time = models.DateTimeField(db_column='Dislike_time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dislikes'

class Likes(models.Model):
    like_id = models.AutoField(db_column='Like_id', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('user.Userdata', models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    video = models.ForeignKey('video.Videodetails', models.DO_NOTHING, db_column='Video_id',related_name="video")  # Field name made lowercase.
    like_time = models.DateTimeField(db_column='Like_time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Likes'