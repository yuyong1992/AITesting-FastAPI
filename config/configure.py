# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/19
import configparser
import threading
import os


class Configure:
    # 单例模式设计
    # 创建一个线程锁对象
    __instance_lock = threading.Lock()
    __flag = False
    __config_file = os.path.abspath(os.path.dirname(__file__)) + '/config.ini'

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls.__instance_lock.acquire()
            if not hasattr(cls, '_instance'):
                cls._instance = super().__new__(cls)
            cls.__instance_lock.release()
        return cls._instance

    def __init__(self):
        if Configure.__flag:
            return
        c = configparser.ConfigParser()
        c.read(Configure.__config_file)

        self.__server = c.get('database', 'server')
        self.__port = c.get('database', 'port')
        self.__user = c.get('database', 'user')
        self.__password = c.get('database', 'password')
        self.__db = c.get('database', 'db')
        Configure.__flag = True

    @property
    def server(self):
        return self.__server

    @property
    def port(self):
        return self.__port

    @property
    def user(self):
        return self.__user

    @property
    def password(self):
        return self.__password

    @property
    def db(self):
        return self.__db


config_data = Configure()
