# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/26
from fastapi import APIRouter

from schemas.api_schema import APICreateSchema, APIUpdateSchema, APIOutputSchema
from crud.crud_api import api as crud
from common.r import R, MyException404, MyException500

router = APIRouter(tags=['api'])


@router.get('/api/{_id}', response_model=APIOutputSchema)
def get_by_id(_id: int):
    api = crud.get_by_id(_id=_id)
    if api is None:
        raise MyException404()
    return R.ok(data=api)


@router.post('/api', response_model=APIOutputSchema)
def save(item: APICreateSchema):
    api = crud.save(schema_in=item)
    if api is None:
        raise MyException404()
    return R.ok(data=api)


@router.put('/api/{_id}', response_model=APIOutputSchema)
def update_by_id(_id: int, item: APIUpdateSchema):
    api = crud.update_by_id(_id=_id, schema_in=item)
    if api is None:
        raise MyException404()
    return R.ok(data=api)


@router.delete('/api/{_id}', response_model=APIOutputSchema)
def remove(_id: int):
    api = crud.remove_by_id(_id=_id)
    if api is None:
        raise MyException404()
    return R.ok(data=api)
