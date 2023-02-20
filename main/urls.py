from django.urls import path,include
from django.contrib import admin 
# from .views import LoginTemplateView
from .views import UserViewSet
from .views import UserApiView
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/userlist/', UserApiView.as_view()),
    # path('login/', LoginTemplateView.as_view(template_name='login.html'), name='login'),
]
