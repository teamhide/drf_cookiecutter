from typing import Union, NoReturn
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from auth.serializers import AuthSerializer, CreateTokenSerializer
from auth.interactors import CreateTokenInteractor


class Auth(APIView):
    def post(self, request: Request) -> Union[Response, NoReturn]:
        """Generate JWT Token"""
        serializer = CreateTokenSerializer(data=request.data)
        if serializer.is_valid():
            token = CreateTokenInteractor().execute(request=serializer.data)
            response = AuthSerializer(token).data
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
