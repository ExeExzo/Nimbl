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
    dislike_id = models.AutoField(db_column='Dislike_id', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey(Userdata, models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    video = models.ForeignKey(Videodetails, models.DO_NOTHING, related_name='video+', db_column='Video_id')  # Field name made lowercase.
    dislike_time = models.DateTimeField(db_column='Dislike_time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dislikes'

class Likes(models.Model):
    like_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Userdata, models.DO_NOTHING)
    video = models.ForeignKey(Videodetails, models.DO_NOTHING, related_name='video+')
    like_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'likes'