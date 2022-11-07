# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/19
from typing import Dict, Any, Optional

from pydantic import BaseSettings, validator
from config.configure import config_data


class Settings(BaseSettings):
    PROJECT_NAME: str = '慧测AITesting自动化平台'
    MYSQL_SERVER: str = config_data.server
    MYSQL_PORT: int = int(config_data.port)
    MYSQL_USER: str = config_data.user
    MYSQL_PASSWORD: str = config_data.password
    MYSQL_DB: str = config_data.db

    SQLALCHEMY_DATABASE_URI: str = None

    @validator('SQLALCHEMY_DATABASE_URI', pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]):
        # 如果连接字符串已经被初始化连接拼接完成，直接返回
        if isinstance(v, str):
            return v

        server = values.get('MYSQL_SERVER')
        port = values.get('MYSQL_PORT')
        user = values.get('MYSQL_USER')
        password = values.get('MYSQL_PASSWORD')
        db = values.get('MYSQL_DB')

        return f'mysql+pymysql://{user}:{password}@{server}:{port}/{db}'

    class Config:
        case_sensitive = True


settings = Settings()
# print(settings.SQLALCHEMY_DATABASE_URI)
