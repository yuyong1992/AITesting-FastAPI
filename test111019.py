# -*- coding: utf-8 -*-
# Created by YUYONG on 2022/10/19

# python 中所有的内容都是对象
import time


def sum():
    print(f'我是一个求和函数')


def fun1(f):
    f()


def how_much_time(f):
    def inner():
        t_start = time.time()
        f()
        t_end = time.time()
        print(f'一共花费了 {t_end - t_start} 秒时间')

    return inner


@how_much_time
def sleep_5s():
    time.sleep(5)
    print('执行结束')


def test01():
    print(f'test01 start')

    def test02():
        print(f'test02')

    print(f'test02 end')


def auth(f):
    def wrapper(*args, **kwargs):
        name = input('input your name>>>').strip()
        pwd = input('input your pwd>>>').strip()
        if name == 'yy' and pwd == '123':
            print(f'登录成功, 欢迎 {name} ！')
            f(*args, **kwargs)
        else:
            print(f'登录失败！')

    return wrapper


@auth
def post_topic(a, b, c):
    print(f'post my content: {a} - {b} - {c}')


if __name__ == '__main__':
    post_topic(1, 2, 3)
