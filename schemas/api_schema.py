# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/26
from datetime import datetime

from pydantic import BaseModel, Json


class APISchema(BaseModel):
    name: str = None
    method: str = 'GET'
    url: str = None
    request_header: str = None
    request_body: str = None
    request_body_type: int = 3
    request_example: str = None
    response_header: str = None
    response_body: str = None
    response_example: str = None
    status: int = 1
    description: str = None
    create_user_id: int = None
    group_id: int = None

    class Config:
        orm_mode = True


class APISelectSchema(APISchema):
    id: int = None
    create_time: datetime = None
    update_time: datetime = None


class APICreateSchema(APISchema):
    pass


class APIUpdateSchema(APISchema):
    pass


class APIRemoveSchema(APISchema):
    pass
