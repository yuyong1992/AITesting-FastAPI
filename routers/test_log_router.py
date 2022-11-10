# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/27

from fastapi import APIRouter

from common.r import R
from schemas.test_log_schema import TestLogSelectSchema, TestLogCreateSchema, TestLogUpdateSchema, TestLogOutputSchema
from crud.crud_test_log import test_log as crud

router = APIRouter(tags=['test_log'])


@router.get('/test-log/{_id}', response_model=TestLogOutputSchema)
def get_by_id(_id: int):
    test_log = crud.get_by_id(_id=_id)
    return R.ok(data=test_log)


@router.post('/test-log', response_model=TestLogOutputSchema)
def save(item: TestLogCreateSchema):
    test_log = crud.save(schema_in=item)
    return R.ok(data=test_log)


@router.put('/test-log/{_id}', response_model=TestLogOutputSchema)
def update_by_id(_id: int, item: TestLogUpdateSchema):
    test_log = crud.update_by_id(_id=_id, schema_in=item)
    return R.ok(data=test_log)


@router.delete('/test-log/{_id}', response_model=TestLogOutputSchema)
def remove(_id):
    test_log = crud.remove_by_id(_id=_id)
    return R.ok(data=test_log)
