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
