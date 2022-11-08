# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/25
from fastapi import APIRouter

from crud.crud_project import project as crud
# import crud.crud_project as crud
from schemas.project_schema import ProjectSelectSchema, ProjectCreateSchema, ProjectUpdateSchema
from common.r import R

router = APIRouter(tags=['project'])


# 完成对项目管理表的增删改查
@router.get('/project/{id}', response_model=ProjectSelectSchema)
def get_by_id(_id: int):
    """
    根据id获取项目数据
    :param _id: 项目id
    :return: ProjectSelectSchema 格式的数据
    """
    project = crud.get_by_id(_id)
    return R.ok(data=project)


@router.post('/project', response_model=ProjectSelectSchema)
def save(item: ProjectCreateSchema):
    """
    保存数据
    :param item: 数据请求体
    :return:
    """
    project = crud.save(item)
    return R.ok(data=project)


@router.put('/project/{id}', response_model=ProjectSelectSchema)
def update_by_id(_id: int, item: ProjectUpdateSchema):
    """
    更新数据
    :param _id: 更新数据的id
    :param item:
    :return:
    """
    project = crud.updata_by_id(_id, item)
    return R.ok(data=project)


@router.delete('/project/{id}', response_model=ProjectSelectSchema)
def remove_by_id(_id: int):
    """
    根据id删除数据
    :param _id: 更新数据的id
    :return:
    """
    project = crud.remove_by_id(_id)
    return R.ok(data=project)
