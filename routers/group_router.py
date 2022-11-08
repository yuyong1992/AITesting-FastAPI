# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/26

from fastapi import APIRouter

from schemas.group_schema import GroupSelectSchema, GroupCreateSchema, GroupUpdateSchema
from crud.crud_group import group as crud
from common.r import R

router = APIRouter(tags=['group'])


@router.get('/group/{id}', response_model=GroupSelectSchema)
def get_by_id(_id: int):
    group = crud.get_by_id(_id=_id)
    return R.ok(data=group)


@router.post('/group', response_model=GroupSelectSchema)
def save(item: GroupCreateSchema):
    group = crud.save(schema_in=item)
    return R.ok(data=group)


@router.put('/group/{id}', response_model=GroupSelectSchema)
def update(_id: int, item: GroupUpdateSchema):
    group = crud.updata_by_id(_id=_id, schema_in=item)
    return R.ok(data=group)


@router.delete('/group/{id}', response_model=GroupSelectSchema)
def remove(_id: int):
    group = crud.remove_by_id(_id=_id)
    return R.ok(data=group)
