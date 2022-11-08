# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/11/8

from crud.crud_base import CRUDBase
from models import TestUser


class CRUDTestUser(CRUDBase):
    pass


test_user = CRUDTestUser(TestUser)
