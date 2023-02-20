from django.contrib import admin
from .models import *
# Register your models here.

class UserdataAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'email', 'username', 'password', 'profile_picture', 'bio','location_name', 'last_login', 'is_authorized', 'is_superuser', 'is_banned']
    list_display_links = ('user_id', 'email', 'username')
    search_fields =('user_id', 'email', 'username')

admin.site.register(Userdata, UserdataAdmin)