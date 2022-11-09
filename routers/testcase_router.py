# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/11/8
from fastapi import APIRouter

from common.r import R
from schemas.testcase_schema import TestcaseSelectSchema, TestcaseCreateSchema, TestcaseUpdateSchema
from crud.crud_testcase import testcase as crud

router = APIRouter(tags=['testcase'])


@router.get('/testcase/{_id}', response_model=TestcaseSelectSchema)
def get_by_id(_id: int):
    testcase = crud.get_by_id(_id=_id)
    return R.ok(data=testcase)


@router.post('/testcase', response_model=TestcaseSelectSchema)
def save(item: TestcaseCreateSchema):
    testcase = crud.save(schema_in=item)
    return R.ok(data=testcase)


@router.put('/testcase/{_id}', response_model=TestcaseSelectSchema)
def update_by_id(_id: int, item: TestcaseUpdateSchema):
    testcase = crud.update_by_id(_id=_id, schema_in=item)
    return R.ok(data=testcase)


@router.delete('/testcase/{_id}', response_model=TestcaseSelectSchema)
def remove_by_id(_id: int):
    testcase = crud.remove_by_id(_id=_id)
    return R.ok(data=testcase)
