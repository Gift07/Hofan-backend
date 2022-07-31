from rest_framework.exceptions import APIException


class NectaError(APIException):
    status_code = 404
    default_detail = "The requested results can not be found"
