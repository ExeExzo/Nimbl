# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class Channeldata(models.Model):
    user = models.ForeignKey('Userdata', models.DO_NOTHING)
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


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Userdata', models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    video = models.ForeignKey('Videodetails', models.DO_NOTHING, db_column='Video_id')  # Field name made lowercase.
    comment_text = models.TextField(db_column='Comment_text')  # Field name made lowercase.
    comment_time = models.DateTimeField(db_column='Comment_time')  # Field name made lowercase.
    parent_comment_id = models.IntegerField(db_column='Parent_comment_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Comment'


class Dislikes(models.Model):
    dislike_id = models.AutoField(db_column='Dislike_id', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('Userdata', models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    video = models.ForeignKey('Videodetails', models.DO_NOTHING, db_column='Video_id')  # Field name made lowercase.
    dislike_time = models.DateTimeField(db_column='Dislike_time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dislikes'


class Likes(models.Model):
    like_id = models.AutoField(db_column='Like_id', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('Userdata', models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    video = models.ForeignKey('Videodetails', models.DO_NOTHING, db_column='Video_id')  # Field name made lowercase.
    like_time = models.DateTimeField(db_column='Like_time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Likes'


class Playlists(models.Model):
    playlist_id = models.AutoField(db_column='Playlist_id', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('Userdata', models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    playlist_name = models.CharField(db_column='Playlist_name', max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='Created_at')  # Field name made lowercase.
    updated_at = models.DateTimeField(db_column='Updated_at')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Playlists'


class Userdata(models.Model):
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    profile_picture = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserData'


class Videoanalytics(models.Model):
    video = models.ForeignKey('Videodetails', models.DO_NOTHING)
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
    uploader = models.ForeignKey(Userdata, models.DO_NOTHING, db_column='uploader')
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
    video = models.ForeignKey(Videodetails, models.DO_NOTHING, db_column='Video_id')  # Field name made lowercase.
    view_time = models.DateTimeField(db_column='View_time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Views'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
