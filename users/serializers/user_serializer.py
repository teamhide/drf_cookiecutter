from projects.serializers import BaseSerializer
from rest_framework import serializers


class UserSerializer(BaseSerializer):
    user_id = serializers.CharField(required=True)
    user_pw = serializers.CharField(required=True)


class UserResponseSerializer(BaseSerializer):
    no = serializers.CharField(required=True)
    user_id = serializers.CharField(required=True)
    user_pw = serializers.CharField(required=True)
