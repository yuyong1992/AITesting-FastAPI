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
                                'code': 2000,
                                'message': message,
                                'data': data
                            })
