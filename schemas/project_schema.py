# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/25
from datetime import datetime

from pydantic import BaseModel


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
