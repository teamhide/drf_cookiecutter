from django.urls import path
from board.views.v1 import Article, ArticleList, Comment


urlpatterns = [
    path('v1/articles/', ArticleList.as_view()),
    path('v1/articles/<int:article_id>', Article.as_view()),
    path('v1/articles/<int:article_id>/comments', Comment.as_view())
]
