# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/26
from crud.crud_base import CRUDBase
from models import Group


class CRUDGroup(CRUDBase):
    pass


group = CRUDGroup(Group)
