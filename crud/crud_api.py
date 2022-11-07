# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/26
from crud.crud_base import CRUDBase
from models import API


class CRUDApi(CRUDBase):
    pass


api = CRUDApi(API)
