# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/11/8
from datetime import datetime

from pydantic import BaseModel

from schemas import BaseOutputSchema


class TestUserSchema(BaseModel):
    username: str
    password: str
    salt: str
    email: str
    mobile: str
    status: bool

    class Config:
        orm_mode = True


class TestUserSelectSchema(TestUserSchema):
    id: int
    create_time: datetime
    update_time: datetime


class TestUserCreateSchema(TestUserSchema):
    pass


class TestUserUpdateSchema(TestUserSchema):
    pass


class TestUserOutputSchema(BaseOutputSchema):
    data: TestUserSelectSchema
