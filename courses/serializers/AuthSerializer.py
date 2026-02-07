# courses/serializers.py
from rest_framework import serializers
from courses.models import User

class AuthSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.CharField(required=False, default='student')

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'role']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email ya está en uso.")
        return value