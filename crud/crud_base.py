# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/25

from fastapi.encoders import jsonable_encoder
from sqlalchemy import text, and_, or_

from db import SessionLocal


class CRUDBase:
    def __init__(self, model):
        """
        初始化需要操作的数据库表模型
        :param model: 当前操作的表模型
        """
        self.model = model

    def get_by_id(self, _id: int):
        """
        根据ID获取数据库数据
        :param _id:
        :return:
        """
        # s: Session = SessionLocal()
        # s.query(self.__model).filter(self.__model.id == _id).first()
        with SessionLocal() as session:
            return session.query(self.model).filter(self.model.id == _id).first()

    def list_by_condition(self, condition):
        """
        根据sql查询条件字符串查询
        :param condition: 符合sql语法的查询条件
        :return:
        """
        with SessionLocal() as session:
            return session.query(self.model).filter(text(condition)).all()

    def list_by_dict_condition_and(self, exact_match=False, **kwargs):
        """
        字典格式的多条件参数查询，条件之间是并的关系
        :param exact_match: 是否精确匹配
        :param kwargs: 查询条件的字典
        :return: 查询资源的列表
        """
        if exact_match:
            condition = {k: v for k, v in kwargs.items() if v}
            with SessionLocal() as session:
                return session.query(self.model).filter_by(**condition).all()
        else:
            condition_list_str = [f'self.model.{k}.like("%{v}%")' for k, v in kwargs.items() if v]
            condition_list = []
            for item in condition_list_str:
                condition_list.append(eval(item))
            with SessionLocal() as session:
                return session.query(self.model).filter(and_(*condition_list)).all()
        # TODO: 按条件查询结果分页

    def list_by_dict_condition_or(self, exact_match=False, **kwargs):
        """
        字典格式的多条件参数查询，条件之间是或的关系
        :param exact_match: 是否精确匹配
        :param kwargs: 查询条件的字典
        :return: 查询资源的列表
        """
        if exact_match:
            condition = {k: v for k, v in kwargs.items() if v}
            with SessionLocal() as session:
                return session.query(self.model).filter_by(**condition).all()
        else:
            condition_list_str = [f'self.model.{k}.like("%v%")' for k, v in kwargs.items() if v]
            condition_list = []
            for item in condition_list_str:
                condition_list.append(item)
            with SessionLocal() as session:
                return session.query(self.model).filter_by(or_(*condition_list)).all()

    def page(self, page_num: int = 0, page_size: int = 100):
        """
        无查询条件分页查询
        :param page_num: 前端要展示的当前页码
        :param page_size: 前端每页展示的数据
        :return: 分页的资源列表
        """
        offset = page_num - 1
        limit = page_size
        with SessionLocal() as session:
            return session.query(self.model).offset(offset).limit(limit).all()

    def save(self, schema_in):
        # 做兼容性类型转换
        schema_in_data = jsonable_encoder(schema_in)
        # 将schema_in_data转换成数据库模型对象
        db_obj = self.model(**schema_in_data)
        with SessionLocal() as session:
            session.add(db_obj)
            session.commit()
            session.refresh(db_obj)
            return db_obj

    def update_by_id(self, _id, schema_in):
        """
        根据id号更新数据
        :param _id:
        :param schema_in:
        :return:
        """
        # 根据id号从数据库读取需要更新的数据
        db_obj = self.get_by_id(_id=_id)
        obj_data = jsonable_encoder(db_obj)
        if isinstance(schema_in, dict):
            update_data = schema_in
        else:
            # exclude_unset=True 过滤不需要更新的数据
            update_data = schema_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        with SessionLocal() as session:
            session.add(db_obj)
            session.commit()
            session.refresh(db_obj)
            return db_obj

    def remove_by_id(self, _id):
        with SessionLocal() as session:
            db_obj = session.query(self.model).get(_id)
            session.delete(db_obj)
            session.commit()
            return db_obj
