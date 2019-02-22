import inject
from typing import List
from rest_framework.utils.serializer_helpers import ReturnDict
from board.entities import ArticleEntity, CommentEntity
from board.repositories import BoardRepository
from projects.converters import Converter


class BoardInteractor:
    @inject.autoparams()
    def __init__(self, board_repository: BoardRepository):
        self.repository = board_repository
        self.converter = Converter()


class CreateArticleInteractor(BoardInteractor):
    def execute(self, request: ReturnDict) -> ArticleEntity:
        user_entity = self.converter.request_to_entity(request=request, entity=ArticleEntity)
        return self.repository.save_article(entity=user_entity)


class GetArticleInteractor(BoardInteractor):
    def execute(self, no: int) -> ArticleEntity:
        return self.repository.get_user(user_id=no)


class ArticleListInteractor(BoardInteractor):
    def execute(self) -> List[ArticleEntity]:
        return self.repository.get_article_list()


class CreateCommentInteractor(BoardInteractor):
    def execute(self, request: ReturnDict, article_id: int) -> ArticleEntity:
        comment_entity = self.converter.request_to_entity(request=request, entity=CommentEntity)
        return self.repository.save_comment(entity=comment_entity, article_id=article_id)
