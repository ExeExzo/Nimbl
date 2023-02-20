from django.urls import path
from . import views

urlpatterns = [
    path('watch/<int:pk>/', views.WatchVideoAPIView.as_view()),
    path('upload/',views.VideoUploadView.as_view()),
    path('category/<str:name>/',views.CategoryAPIView.as_view()),
    path('category/',views.CategoryListAPIView.as_view()),
    # path('upload/')
]

