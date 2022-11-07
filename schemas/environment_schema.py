# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/25
from datetime import datetime
from typing import Dict

from pydantic import BaseModel


class EnvironmentSchema(BaseModel):
    name: str = None
    base_url: str = None
    verify: int = '0'
    variables: Dict = {}
    parameters: Dict = {}
    project_id: int = None

    class Config:
        orm_mode = True


class EnvironmentSelectSchema(EnvironmentSchema):
    id: int
    create_time: datetime = None
    update_time: datetime = None


class EnvironmentUpdateSchema(EnvironmentSchema):
    pass


class EnvironmentCreateSchema(EnvironmentSchema):
    pass
