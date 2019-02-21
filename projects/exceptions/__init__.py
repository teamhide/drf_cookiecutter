from rest_framework.exceptions import APIException


class BaseAPIException(APIException):
    pass


class NotFoundException(BaseAPIException):
    status_code = 404
    default_code = 'not_found'
    default_detail = 'can not found resource'


class UnknownFieldException(BaseAPIException):
    status_code = 400
    default_code = 'unknown_field'
    default_detail = 'unknown field error'


class DoNotHavePermission(BaseAPIException):
    status_code = 401
    default_code = 'permission_denied'
    default_detail = 'permission denied'


class InvalidRequestType(BaseAPIException):
    status_code = 405
    default_code = 'invalid_request_type'
    default_detail = 'invalid request type'
