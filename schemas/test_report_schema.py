#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime

from pydantic import BaseModel


class TestReportSchema(BaseModel):
    name: str
    type: bool
    status: bool
    project_id: int
    create_user_id: int


class TestReportSelectSchema(TestReportSchema):
    id: int
    create_time: datetime
    update_time: datetime


class TestReportCreateSchema(TestReportSchema):
    pass


class TestReportUpdateSchema(TestReportSchema):
    pass
