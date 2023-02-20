from django.db import models

# Create your models here.

class Userdata(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    profile_picture = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    location_name = models.CharField(max_length=255, blank=True, null=True)
    last_login = models.DateField(blank=True, null=True)
    is_authorized = models.BooleanField(blank=True, null=True)
    is_superuser = models.BooleanField(blank=True, null=True)
    is_banned = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userdata'