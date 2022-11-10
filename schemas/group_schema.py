# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/26
from datetime import datetime
from pydantic import BaseModel

from schemas import BaseOutputSchema


class GroupSchema(BaseModel):
    name: str = None
    type: int = 1
    project_id: int = None

    class Config:
        orm_mode = True


class GroupSelectSchema(GroupSchema):
    id: int
    create_time: datetime = None
    update_time: datetime = None


class GroupCreateSchema(GroupSchema):
    pass


class GroupUpdateSchema(GroupSchema):
    pass


class GroupOutputSchema(BaseOutputSchema):
    data: GroupSelectSchema
