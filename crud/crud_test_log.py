# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/27
from crud.crud_base import CRUDBase
from models import TestLog


class CRUDTestLog(CRUDBase):
    pass


test_log = CRUDTestLog(TestLog)

