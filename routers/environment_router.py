# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/25
from fastapi import APIRouter

from common.r import R
from schemas.environment_schema import EnvironmentCreateSchema, EnvironmentUpdateSchema, EnvironmentSelectSchema
from crud.crud_environment import environment as crud

router = APIRouter(tags=['environment'])


@router.get('/environment/{id}', response_model=EnvironmentSelectSchema)
def get_by_id(_id: int):
    environment = crud.get_by_id(_id=_id)
    return environment


@router.get('/environment', response_model=list[EnvironmentSelectSchema])
def get_by_project_id(_id: int):
    """
    根据project_id查询environment列表
    :param _id: project_id
    :return:
    """
    environments = crud.list_by_project_id(_id=_id)
    return R.ok(data=environments)


@router.post('/environment', response_model=EnvironmentSelectSchema)
def save(item: EnvironmentCreateSchema):
    environment = crud.save(schema_in=item)
    return environment


@router.put('/environment/{id}', response_model=EnvironmentSelectSchema)
def update(_id: int, item: EnvironmentUpdateSchema):
    environment = crud.updata_by_id(_id=_id, schema_in=item)
    return environment


@router.delete('/environment/{id}', response_model=EnvironmentSelectSchema)
def remove_by_id(_id):
    environment = crud.remove_by_id(_id=_id)
    return environment
