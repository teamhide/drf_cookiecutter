from typing import Union, NoReturn
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from users.serializers import UserSerializer, UserResponseSerializer
from users.interactors import CreateUserInteractor, GetUserInteractor, UserListInteractor
from users.dtos import CreateUserDto


class User(APIView):
    def get(self, request: Request, no: int) -> Union[Response, NoReturn]:
        """Get a User"""
        user = GetUserInteractor().execute(no=no)
        if user:
            return Response(status=status.HTTP_200_OK, data=user.__dict__)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserList(APIView):
    def get(self, request: Request) -> Union[Response, NoReturn]:
        """Get User List"""
        users = UserListInteractor().execute()
        serializer = UserResponseSerializer(users, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request: Request) -> Union[Response, NoReturn]:
        """Create User"""
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = CreateUserInteractor().execute(dto=CreateUserDto(**serializer.data))
            response = UserResponseSerializer(user).data
            return Response(status=status.HTTP_200_OK, data=response)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
