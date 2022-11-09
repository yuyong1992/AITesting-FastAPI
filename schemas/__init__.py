# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/19
from pydantic import BaseModel


class BaseOutputSchema(BaseModel):
    code: int = 200
    message: str = 'success'
