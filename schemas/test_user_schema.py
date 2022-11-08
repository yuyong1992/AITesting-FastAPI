# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/11/8
from datetime import datetime

from pydantic import BaseModel


class TestUserSchema(BaseModel):
    username: str
    password: str
    salt: str
    email: str
    mobile: str
    status: bool


class TestUserSelectSchema(BaseModel):
    id: int
    create_time: datetime
    update_time: datetime


class TestUserCreateSchema(BaseModel):
    pass


class TestUserUpdateSchema(BaseModel):
    pass
