from django.db import models
from user.models import Userdata
from video.models import Videoanalytics, Videodetails

# Create your models here.

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Userdata, models.DO_NOTHING)
    video = models.ForeignKey(Videodetails, models.DO_NOTHING, related_name='video+')
    comment_text = models.TextField()
    comment_time = models.DateTimeField()
    parent_comment_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'comment'

class Dislikes(models.Model):
    dislike_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Userdata, models.DO_NOTHING)
    video = models.ForeignKey(Videodetails, models.DO_NOTHING, related_name='video+')
    dislike_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dislikes'

class Likes(models.Model):
    like_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Userdata, models.DO_NOTHING)
    video = models.ForeignKey(Videodetails, models.DO_NOTHING, related_name='video+')
    like_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'likes'