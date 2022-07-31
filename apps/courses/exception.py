from rest_framework.exceptions import APIException


class CourseNotFound(APIException):
    status_code = 404
    default_detail = "the requested course does not exist"
