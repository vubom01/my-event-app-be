from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from starlette import status
from starlette.responses import JSONResponse
from fastapi import Request

from app.schemas.sche_base import ResponseSchemaBase


class CustomException(Exception):
    http_code: int
    code: str
    message: str

    def __init__(self, http_code: int = None, code: str = None, message: str = None):
        self.http_code = http_code if http_code else 500
        self.code = code if code else str(self.http_code)
        self.message = message


class ValidateException(CustomException):

    def __init__(self, code: str = None, message: str = None):
        self.http_code = 400
        self.code = code if code else str(self.http_code)
        self.message = message


async def fastapi_error_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content=jsonable_encoder(ResponseSchemaBase().custom_response(
            '500', "Có lỗi xảy ra, vui lòng liên hệ admin!"))
    )


async def http_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.http_code,
        content=jsonable_encoder(
            ResponseSchemaBase().custom_response(exc.code, exc.message))
    )


def get_message_validation(exc):
    message = ""
    for error in exc.errors():
        message += "/'" + str(error.get("loc")
                              [1]) + "'/" + ': ' + error.get("msg") + ", "

    message = message[:-2]

    return message


def get_message(errors: dict) -> str:
    loc = errors.get("loc")
    msg = errors.get("msg")
    type = errors.get("type")
    return loc[0] + ": " + loc[1] + " " + msg + ", type: " + type


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            {"code": "001", "message": get_message(exc.errors()[0])}),
    )


class ObjectNotFound(CustomException):
    def __init__(self, obj: str):
        super().__init__(http_code=400, code="404", message=f"{obj} not found")


class UrlNotFound(CustomException):
    def __init__(self, obj: str):
        super().__init__(http_code=404, code="404", message=f"{obj} not found")


class FieldIsRequired(CustomException):
    def __init__(self, field_name: str):
        super().__init__(http_code=400, code="402", message=f"{field_name} is required")


class URLNotFound(CustomException):
    def __init__(self, url: str):
        super().__init__(http_code=404, code="404", message=f"{url} not found")


class InvalidFieldFormat(CustomException):
    def __init__(self, field_name: str):
        super().__init__(http_code=400, code="417", message=f"{field_name} format is invalid")


class InvalidField(CustomException):
    def __init__(self, field_name: str):
        super().__init__(http_code=400, code="420", message=f"{field_name} is invalid")


class Unauthorized(CustomException):
    def __init__(self):
        super().__init__(http_code=401, code="401", message=f"Unauthorized")


class PermissionDenied(CustomException):
    def __init__(self):
        super().__init__(http_code=403, code="403", message=f"Permission denied")


class InternalServerError(CustomException):
    def __init__(self):
        super().__init__(http_code=500, code="500", message="Internal server error")
