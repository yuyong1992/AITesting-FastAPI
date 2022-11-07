# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/25
from crud.crud_base import CRUDBase
from models import Environment


class CRUDEnvironment(CRUDBase):
    def list_by_project_id(self, _id):
        return self.list_by_condition(f'project_id={_id}')


environment = CRUDEnvironment(Environment)
