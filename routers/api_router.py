# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/26
from fastapi import APIRouter

from schemas.api_schema import APISelectSchema, APICreateSchema, APIUpdateSchema
from crud.crud_api import api as crud
from common.r import R

router = APIRouter(tags=['api'])


@router.get('/api/{id}', response_model=APISelectSchema)
def get_by_id(_id: int):
    api = crud.get_by_id(_id=_id)
    return R.ok(data=api)


@router.post('/api', response_model=APISelectSchema)
def save(item: APICreateSchema):
    api = crud.save(schema_in=item)
    return R.ok(data=api)


@router.put('/api/{id}', response_model=APISelectSchema)
def update_by_id(_id: int, item: APIUpdateSchema):
    api = crud.updata_by_id(_id=_id, schema_in=item)
    return R.ok(data=api)


@router.delete('/api/{id}', response_model=APISelectSchema)
def remove(_id: int):
    api = crud.remove_by_id(_id=_id)
    return R.ok(data=api)
