#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import APIRouter

from common.r import R
from crud.crud_test_report import test_report as crud
from schemas.test_report_schema import TestReportSelectSchema, TestReportCreateSchema, TestReportUpdateSchema

router = APIRouter(tags=['test_report'])


@router.get('/test_report/{id}', response_model=TestReportSelectSchema)
def get_by_id(_id):
    """
    根据id获取test_report

    :param _id: id of test_report
    :return: test_report
    """
    test_report = crud.get_by_id(_id=_id)
    return R.ok(data=test_report)


@router.post('/test_report', response_model=TestReportSelectSchema)
def save(item: TestReportCreateSchema):
    test_report = crud.save(schema_in=item)
    return R.ok(data=test_report)


@router.put('/test_report/{id}', response_model=TestReportSelectSchema)
def update_by_id(_id: int, item: TestReportUpdateSchema):
    """
    根据id更新test_report
    :param _id: id of test_report
    :param item: content to update
    :return: test_report
    """
    test_report = crud.updata_by_id(_id=_id, schema_in=item)
    return R.ok(data=test_report)


@router.delete('/test_report/{id}', response_model=TestReportSelectSchema)
def remove_by_id(_id: int):
    test_report = crud.remove_by_id(_id=_id)
    return R.ok(data=test_report)
