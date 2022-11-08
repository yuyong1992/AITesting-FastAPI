# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/11/8

from crud.crud_base import CRUDBase
from models import Testcase


class CRUDTestcase(CRUDBase):
    pass


testcase = CRUDTestcase(model=Testcase)
