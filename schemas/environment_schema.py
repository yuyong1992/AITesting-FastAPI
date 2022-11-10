# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/25
from datetime import datetime
from typing import Dict, List

from pydantic import BaseModel

from schemas import BaseOutputSchema


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


class EnvironmentOutputSchema(BaseOutputSchema):
    data: EnvironmentSelectSchema


class EnvironmentListOutputSchema(BaseOutputSchema):
    # List 在python 3.9版本后可以直接使用内置的list类型
    data: List[EnvironmentSelectSchema]
