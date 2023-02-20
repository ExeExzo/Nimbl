#changed

from django.contrib.auth import authenticate
from django.utils import timezone
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password

#
from .serializers import RegistrationSerializers
from .models import Userdata
#

class UserRegistrationView(CreateAPIView):
    queryset = Userdata.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializers

#   Hashing
    def perform_create(self, serializer):
        serializer.save()


class UserLoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = Userdata.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed("email is wrong")
        if check_password(password,user.password):
            user.is_authorized = True
            user.last_login = timezone.now()
            user.save()
            return Response({"message": "Login successful"})
        else:
            return Response({"error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)




class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = authenticate(username=request.user.username, password=request.data.get('old_password'))
        if user is None:
            return Response({'error': 'Invalid old password'}, status=status.HTTP_400_BAD_REQUEST)

        new_password = request.data.get('new_password')
        if not new_password:
            return Response({'error': 'New password is required'}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()

        return Response({'success': 'Password changed successfully'}, status=status.HTTP_200_OK)