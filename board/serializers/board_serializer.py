from rest_framework import serializers
from projects.serializers import BaseSerializer
from users.serializers import UserSerializer


class CommentSerializer(BaseSerializer):
    user_id = serializers.CharField()
    body = serializers.CharField()


class ArticleSerializer(BaseSerializer):
    user_id = serializers.CharField()
    subject = serializers.CharField()
    body = serializers.CharField()
    password = serializers.CharField()


class ArticleResponseSerializer(BaseSerializer):
    user_id = serializers.CharField()
    subject = serializers.CharField()
    body = serializers.CharField()
    comments = serializers.ListField()
    password = serializers.CharField()
