# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/11/8
from datetime import datetime

from pydantic import BaseModel

from schemas import BaseOutputSchema


class TestcaseSchema(BaseModel):
    name: str
    file_name: str
    priority: str
    tags: str
    status: str
    steps: str
    group_id: int

    class Config:
        orm_mode = True


class TestcaseSelectSchema(TestcaseSchema):
    id: int
    create_time: datetime
    update_time: datetime


class TestcaseCreateSchema(TestcaseSchema):
    pass


class TestcaseUpdateSchema(TestcaseSchema):
    pass


class TestcaseOutputSchema(BaseOutputSchema):
    data: TestcaseSelectSchema
