from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        # Extract and remove 'password2' from validated_data
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')

        if password != password2:
            raise serializers.ValidationError({"password": "Passwords do not match."})

        # Create the user
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user
