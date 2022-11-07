# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/25
from crud.crud_base import CRUDBase
from models import Project


class CRUDProject(CRUDBase):
    pass


project = CRUDProject(Project)
