from typing import Union, NoReturn
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from users.serializers import UserSerializer, UserResponseSerializer
from board.serializers import ArticleSerializer, CommentSerializer, ArticleResponseSerializer
from board.interactors import CreateArticleInteractor, GetArticleInteractor, ArticleListInteractor,\
    CreateCommentInteractor


class Article(APIView):
    def get(self, request: Request, no: int) -> Union[Response, NoReturn]:
        pass


class ArticleList(APIView):
    def get(self, request: Request) -> Union[Response, NoReturn]:
        articles = ArticleListInteractor().execute()
        if articles:
            serializer = ArticleResponseSerializer(articles, many=True)
            print(serializer.data)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request: Request) -> Union[Response, NoReturn]:
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            article = CreateArticleInteractor().execute(request=serializer.data)
            response = ArticleResponseSerializer(article).data
            return Response(status=status.HTTP_200_OK, data=response)
        else:
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Comment(APIView):
    def post(self, request: Request, article_id: int) -> Union[Response, NoReturn]:
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            comment = CreateCommentInteractor().execute(request=serializer.data, article_id=article_id)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
