# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/23
from sqlalchemy import Column, Integer, String, JSON, ForeignKey, Text, Boolean, Float

from db import Base


class Project(Base):
    __tablename__ = 'hc_project'
    id = Column(Integer, primary_key=True, autoincrement='auto')
    name = Column(String, nullable=False, index=True)
    type = Column(String, nullable=False)
    version = Column(String, nullable=True)
    remark = Column(String, nullable=True)


class Environment(Base):
    __tablename__ = 'hc_environment'
    id = Column(Integer, primary_key=True, autoincrement='auto')
    name = Column(String, nullable=False, index=True)
    base_url = Column(String, nullable=False)
    verify = Column(Boolean, nullable=True, default=False)
    variables = Column(JSON, nullable=True)
    parameters = Column(JSON, nullable=True)
    project_id = Column(Integer, ForeignKey('hc_project.id'), nullable=True)


class Group(Base):
    __tablename__ = 'hc_group'
    id = Column(Integer, primary_key=True, autoincrement='auto')
    name = Column(String, nullable=False, index=True)
    type = Column(Integer, nullable=False)
    project_id = Column(Integer, ForeignKey('hc_project.id'), nullable=True)


class API(Base):
    __tablename__ = 'hc_api'
    id = Column(Integer, primary_key=True, autoincrement='auto')
    name = Column(String, nullable=False)
    method = Column(String, nullable=False)
    url = Column(String, nullable=False)
    request_header = Column(JSON)
    request_body = Column(JSON)
    request_body_type = Column(Integer)
    request_example = Column(Text)
    response_header = Column(JSON)
    response_body = Column(JSON)
    response_example = Column(Text)
    status = Column(Integer)
    description = Column(String)
    create_user_id = Column(Integer)
    group_id = Column(Integer, ForeignKey('hc_group.id'))


class TestLog(Base):
    __tablename__ = 'hc_test_log'
    id = Column(Integer, primary_key=True, autoincrement='auto')
    status = Column(Boolean, nullable=False)
    name = Column(String, nullable=False)
    summary = Column(JSON)
    duration = Column(Float)
    testcase_id = Column(Integer, ForeignKey('hc_testcase.id'))


class TestReport(Base):
    __tablename__ = 'hc_test_report'
    id = Column(Integer, primary_key=True, autoincrement='auto')
    name = Column(String, nullable=False)
    type = Column(Boolean, nullable=False)
    status = Column(Boolean, nullable=False)
    project_id = Column(Integer, ForeignKey('hc_project.id'))
    create_user_id = Column(Integer, ForeignKey('hc_user.id'))
