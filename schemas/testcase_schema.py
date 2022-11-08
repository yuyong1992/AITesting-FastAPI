# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/11/8
from datetime import datetime

from pydantic import BaseModel


class TestcaseSchema(BaseModel):
    name: str
    file_name: str
    priority: str
    tags: str
    status: str
    steps: str
    group_id: int


class TestcaseSelectSchema(BaseModel):
    id: int
    create_time: datetime
    update_time: datetime


class TestcaseCreateSchema(BaseModel):
    pass


class TestcaseUpdateSchema(BaseModel):
    pass
