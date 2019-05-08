from rest_framework import serializers
from projects.exceptions import UnknownFieldException


class BaseSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, attrs):
        unknown = set(self.initial_data) - set(self.fields)
        if unknown:
            raise UnknownFieldException
        return attrs
