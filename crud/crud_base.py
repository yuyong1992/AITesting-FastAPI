# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/25
from fastapi.encoders import jsonable_encoder
from sqlalchemy import text

from db import SessionLocal


class CRUDBase:
    def __init__(self, model):
        """
        初始化需要操作的数据库表模型
        :param model: 表模型
        """
        self.__model = model

    def get_by_id(self, _id: int):
        """
        根据ID获取数据库数据
        :param _id:
        :return:
        """
        # s: Session = SessionLocal()
        # s.query(self.__model).filter(self.__model.id == _id).first()
        with SessionLocal() as session:
            return session.query(self.__model).filter(self.__model.id == _id).first()

    def list_by_condition(self, condition):
        """
        根据sql查询条件字符串查询
        :param condition: 符合sql语法的查询条件
        :return:
        """
        with SessionLocal() as session:
            return session.query(self.__model).filter(text(condition)).all()

    def page(self, skip: int = 0, limit: int = 100):
        """
        无查询条件分页查询
        :param skip:
        :param limit:
        :return:
        """
        with SessionLocal() as session:
            return session.query(self.__model).offset(skip).limit(limit).all()

    def save(self, schema_in):
        # 做兼容性类型转换
        schema_in_data = jsonable_encoder(schema_in)
        # 将schema_in_data转换成数据库模型对象
        db_obj = self.__model(**schema_in_data)
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
            db_obj = session.query(self.__model).get(_id)
            session.delete(db_obj)
            session.commit()
            return db_obj
