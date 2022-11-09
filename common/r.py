# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/26

from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse


class R:
    @staticmethod
    def ok(message='success', data=None):
        data = jsonable_encoder(data)
        return JSONResponse(status_code=200,
                            content={
                                'code': 200,
                                'message': message,
                                'data': data
                            })

    @staticmethod
    def err_404(message='资源不存在'):
        return JSONResponse(status_code=200,
                            content={
                                'code': 404,
                                'message': message,
                            })


class MyException404(Exception):
    def __init__(self, code=404, message='资源不存在'):
        self.code = code
        self.message = message
