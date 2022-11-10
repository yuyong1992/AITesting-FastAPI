# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/26

from fastapi import APIRouter

from schemas.group_schema import GroupSelectSchema, GroupCreateSchema, GroupUpdateSchema, GroupOutputSchema
from crud.crud_group import group as crud
from common.r import R, MyException404

router = APIRouter(tags=['group'])


@router.get('/group/{_id}', response_model=GroupOutputSchema)
def get_by_id(_id: int):
    group = crud.get_by_id(_id=_id)
    if group is None:
        raise MyException404()
    return R.ok(data=group)


@router.post('/group', response_model=GroupOutputSchema)
def save(item: GroupCreateSchema):
    group = crud.save(schema_in=item)
    if group is None:
        raise MyException404()
    return R.ok(data=group)


@router.put('/group/{_id}', response_model=GroupOutputSchema)
def update(_id: int, item: GroupUpdateSchema):
    group = crud.update_by_id(_id=_id, schema_in=item)
    if group is None:
        raise MyException404()
    return R.ok(data=group)


@router.delete('/group/{_id}', response_model=GroupOutputSchema)
def remove(_id: int):
    group = crud.remove_by_id(_id=_id)
    if group is None:
        raise MyException404()
    return R.ok(data=group)
