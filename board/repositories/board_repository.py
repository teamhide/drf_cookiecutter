import abc
from datetime import datetime
from typing import List, Union, NoReturn
from users.models.mongo import User
from board.models.mongo import Article, Comment
from board.entities import ArticleEntity, CommentEntity
from projects.exceptions import NotFoundException, AlreadyExistException
from projects.converters import Converter


class BoardRepository:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def _find_article(self, article_id: int) -> Article:
        raise NotImplementedError

    @abc.abstractmethod
    def get_article(self, article_id: int) -> ArticleEntity:
        raise NotImplementedError

    @abc.abstractmethod
    def get_article_list(self) -> List[ArticleEntity]:
        raise NotImplementedError

    @abc.abstractmethod
    def save_article(self, entity: ArticleEntity) -> Union[ArticleEntity, NoReturn]:
        raise NotImplementedError

    @abc.abstractmethod
    def save_comment(self, entity: CommentEntity, article_id: int) -> ArticleEntity:
        raise NotImplementedError


class BoardMongoRepository(BoardRepository):
    def __init__(self):
        self.converter = Converter()
        self.current_time = datetime.now().replace(microsecond=0)

    def _find_article(self, article_id: int) -> Article:
        raise NotImplementedError

    def get_article(self, article_id: int) -> ArticleEntity:
        raise NotImplementedError

    def get_article_list(self) -> List[ArticleEntity]:
        articles = Article.objects.all()
        article_entity = []
        for article in articles:
            article_entity.append(self.converter.model_to_entity(model=article, entity=ArticleEntity))
        return article_entity

    def save_article(self, entity: ArticleEntity) -> Union[ArticleEntity, NoReturn]:
        user = User.objects(user_id=entity.user_id).first()
        if user is None:
            raise NotFoundException

        article = Article(
            user_id=user,
            subject=entity.subject,
            body=entity.body,
            comments=[],
            password=entity.password,
            created_at=self.current_time,
            updated_at=self.current_time
        ).save()
        return self.converter.model_to_entity(model=article, entity=ArticleEntity)

    def save_comment(self, entity: CommentEntity, article_id: int) -> ArticleEntity:
        article = Article.objects(article_id=article_id).first()
        user = User.objects(user_id=entity.user_id).first()
        if article is None or user is None:
            raise NotFoundException

        comment = Comment(
            user_id=user,
            body=entity.body
        )

        article.comments.append(comment)
        article.save()

        return self.converter.model_to_entity(model=article, entity=ArticleEntity)
