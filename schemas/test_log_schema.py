# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/27
from datetime import datetime
from typing import Dict

from pydantic import BaseModel


class TestLogSchema(BaseModel):
    name: str = None
    summary: Dict = None
    duration: float = None
    testcase_id: int = None


class TestLogSelectSchema(TestLogSchema):
    id: int
    create_time: datetime
    update_time: datetime


class TestLogCreateSchema(TestLogSchema):
    pass


class TestLogUpdateSchema(TestLogSchema):
    pass


class TestLogResponseSchema(TestLogSchema):
    pass
