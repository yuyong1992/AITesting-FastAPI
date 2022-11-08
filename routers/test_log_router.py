# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/27

from fastapi import APIRouter

from common.r import R
from schemas.test_log_schema import TestLogSelectSchema, TestLogCreateSchema, TestLogUpdateSchema
from crud.crud_test_log import test_log as crud

router = APIRouter(tags=['test_log'])


@router.get('/test_log/{id}', response_model=TestLogSelectSchema)
def get_by_id(_id: int):
    test_log = crud.get_by_id(_id=_id)
    return R.ok(data=test_log)


@router.post('/test_log', response_model=TestLogSelectSchema)
def save(item: TestLogCreateSchema):
    test_log = crud.save(schema_in=item)
    return R.ok(data=test_log)


@router.put('/test_log/{id}', response_model=TestLogSelectSchema)
def update_by_id(_id: int, item: TestLogUpdateSchema):
    test_log = crud.updata_by_id(_id=_id, schema_in=item)
    return R.ok(data=test_log)


@router.delete('/test_log/{id}', response_model=TestLogSelectSchema)
def remove(_id):
    test_log = crud.remove_by_id(_id=_id)
    return R.ok(data=test_log)
