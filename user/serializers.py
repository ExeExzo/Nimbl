#changed
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from rest_framework import serializers
from .models import Userdata
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password,check_password

# class LoginSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Userdata
#         fields= ['username','password']

def validate_password(password):
    errors = []

    # Password must be at least 8 characters long
    if len(password) < 8:
        errors.append(_('Password must be at least 8 characters long.'))

    # Password must contain both letters and numbers
    if not any(char.isdigit() for char in password):
        errors.append(_('Password must contain at least one digit.'))

    if not any(char.isalpha() for char in password):
        errors.append(_('Password must contain at least one letter.'))

    # Password cannot be too common
    common_passwords = [
        'password', '123456', 'qwerty', 'letmein', 'admin', 'abc123'
    ]
    if password.lower() in common_passwords:
        errors.append(_('Password is too common. Please choose a different password.'))

    if errors:
        raise ValidationError(errors)



class RegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Userdata
        exclude =('user_id','is_authorized','is_banned','is_superuser')
        extra_kwargs = {
            'password':{'write_only' : True}
        }

    def create(self, validated_data):
        # Get the password from the validated data
        password = validated_data.get('password')
        email = validated_data.get('email')

        # Call the custom validate_password function to validate the password
        try:
            validate_password(password)
            validate_email(email)
        except ValidationError as e:
            # Raise a ValidationError with the error messages from the custom validator
            raise serializers.ValidationError(str(e))

        # Create the model instance
        user = Userdata.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            password=make_password(validated_data['password']),
            is_authorized = True,
        )
        return user

