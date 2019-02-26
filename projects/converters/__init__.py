from django.http.request import QueryDict
from rest_framework.request import Request
from rest_framework.utils.serializer_helpers import ReturnDict
from projects.exceptions import InvalidRequestType
from board.models.mongo import Comment


class Converter:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Converter, cls).__new__(cls)
        return cls.instance

    def remove_none_from_dict(self, obj) -> dict:
        return dict(filter(lambda x: x[1], obj.items()))

    def entity_to_model(self, entity, model):
        return model(**entity.__dict__)

    def model_to_entity(self, model, entity):
        model_dict = dict(**model._data)
        if 'id' in model_dict:
            model_dict.pop('id')
        if 'comments' in model_dict:
            comment_dict = []
            for comment in model_dict['comments']:
                comment_dict.append(self._comment_to_dict(comment=comment))
            model_dict['comments'] = comment_dict
        return entity(**model_dict)

    def request_to_entity(self, request, entity):
        if type(request) is QueryDict:
            return entity(**request.dict())
        elif type(request) is dict:
            return entity(**request)
        elif type(request) is Request:
            return entity(**request)
        elif type(request) is ReturnDict:
            return entity(**request)
        else:
            raise InvalidRequestType

    def _comment_to_dict(self, comment: Comment):
        from board.serializers import CommentSerializer
        comment = CommentSerializer(comment)
        return comment.data
