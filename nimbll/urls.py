from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from user.views import UserRegistrationView,UserLoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('', include ('main.urls')),
    path('admin/', admin.site.urls),
    path('login/' , UserLoginView.as_view()),
    path('register/', UserRegistrationView.as_view()),
    # path('', include('main.urls')),
    # path('', include('channel.urls')),
    # path('', include('feedback.urls')),
    # path('', include('user.urls')),
    # path('', include('video.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

admin.site.index_title = "Nimbl"
admin.site.site_header = "Nimbl"
admin.site.site_title = "Nimbl"
