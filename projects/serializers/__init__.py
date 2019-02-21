from rest_framework import serializers
from projects.exceptions import UnknownFieldException


class BaseSerializer(serializers.Serializer):
    """Check if unknown field exists"""
    def validate(self, attrs):
        unknown = set(self.initial_data) - set(self.fields)
        if unknown:
            raise UnknownFieldException
        return attrs
