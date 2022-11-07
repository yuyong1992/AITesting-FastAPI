# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/23

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config.settings import settings

# 创建一个数据库访问引擎对象，根据数据库连接字符串
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)

# 创建会话对象 -- 对数据的操作对象
# 创建Session对象的代码：session = SessionLocal()
# 创建对象：session = 类名()
# session = 对象名() 默认会执行 该桂香所属的类的 __all__ 方法
SessionLocal = sessionmaker(autocommit=False, expire_on_commit=False, bind=engine)

# 动态创建数据库model的基类，数据库model只需要继承该类，就可以完成model到数据库表之间的映射
Base = declarative_base()
