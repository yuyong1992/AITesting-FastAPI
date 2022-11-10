# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/11/8

from fastapi import APIRouter

from common.r import R, MyException404
from schemas.test_user_schema import TestUserSelectSchema, TestUserCreateSchema, TestUserUpdateSchema, \
    TestUserOutputSchema
from crud.crud_test_user import test_user as crud

router = APIRouter(tags=['test-user'])


@router.get('/test-user/{_id}', response_model=TestUserOutputSchema)
def get_by_id(_id: int):
    test_user = crud.get_by_id(_id=_id)
    if test_user is None:
        raise MyException404()
    return R.ok(data=test_user)


@router.post('/test-user', response_model=TestUserOutputSchema)
def save(item: TestUserCreateSchema):
    test_user = crud.save(schema_in=item)
    if test_user is None:
        raise MyException404()
    return R.ok(data=test_user)


@router.put('/test-user/{_id}', response_model=TestUserOutputSchema)
def update_by_id(_id: int, item: TestUserUpdateSchema):
    test_user = crud.update_by_id(_d=_id, schema_in=item)
    if test_user is None:
        raise MyException404()
    return R.ok(data=test_user)


@router.delete('/test-user/{_id}', response_model=TestUserOutputSchema)
def remove_by_id(_id: int):
    test_user = crud.remove_by_id(_id=_id)
    if test_user is None:
        raise MyException404()
    return R.ok(data=test_user)
