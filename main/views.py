from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from main.serializers import UserSerializer
from rest_framework import viewsets
from main.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.settings import api_settings
from django.contrib.auth import authenticate
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.

# class LoginTemplateView(TemplateView):
#     template_name = 'login.html'

#     def post(self, request, *args, **kwargs):
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             return render(request, self.template_name, {'error': 'Invalid login credentials.'})

class UserApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all() # quersyset ozgertu kerek
    permission_classes = (IsAdminUser,)