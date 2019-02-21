from projects.serializers import BaseSerializer
from rest_framework import serializers


class AuthSerializer(BaseSerializer):
    token = serializers.CharField(required=True)


class CreateTokenSerializer(BaseSerializer):
    user_id = serializers.CharField(required=True)
    user_pw = serializers.CharField(required=True)
