#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from crud.crud_base import CRUDBase
from models import TestReport


class CRUDTestReport(CRUDBase):
    pass


test_report = CRUDTestReport(TestReport)
