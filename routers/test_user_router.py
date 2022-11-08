# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/11/8

from fastapi import APIRouter

from common.r import R
from schemas.test_user_schema import TestUserSelectSchema, TestUserCreateSchema, TestUserUpdateSchema
from crud.crud_test_user import test_user as crud

router = APIRouter(tags=['test_user'])


@router.get('/test_user/{id}', response_model=TestUserSelectSchema)
def get_by_id(_id: int):
    test_user = crud.get_by_id(_id=_id)
    return R.ok(data=test_user)


@router.post('/test_user', response_model=TestUserSelectSchema)
def save(item: TestUserCreateSchema):
    test_user = crud.save(schema_in=item)
    return R.ok(data=test_user)


@router.put('/test_user/{id}', response_model=TestUserSelectSchema)
def update_by_id(_id: int, item: TestUserUpdateSchema):
    test_user = crud.update_by_id(_d=_id, schema_in=item)
    return R.ok(data=test_user)


@router.delete('/test_user/{id}')
def remove_by_id(_id: int):
    test_user = crud.remove_by_id(_id=_id)
    return R.ok(data=test_user)
