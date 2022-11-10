# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/25
from datetime import datetime
from typing import List

from pydantic import BaseModel

from schemas import BaseOutputSchema


class ProjectSchema(BaseModel):
    name: str = None
    type: str = 'Web'
    version: str = '2.0'
    remark: str = '慧测AITestiong自动化平台'

    class Config:
        orm_mode = True


class ProjectSelectSchema(ProjectSchema):
    id: int
    create_time: datetime = None
    update_time: datetime = None


class ProjectUpdateSchema(ProjectSchema):
    pass


class ProjectCreateSchema(ProjectSchema):
    pass


class ProjectOutputSchema(BaseOutputSchema):
    data: ProjectSchema


class ProjectListOutputSchema(BaseOutputSchema):
    data: List[ProjectSelectSchema]
