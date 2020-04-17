# coding=utf-8

"""
配置文件
"""

# redis config

HOST = "localhost"
PORT = 6379
DB = 3
PHONE = 'phone'
PWD = 'pwd'
CARD = 'card'
COOKIE = 'cookies'
LOGIN_CODE = 'login_code'
VERIFY_CODE = 'verify_code'
IS_LOGIN = 'is_login'
CHECK_LOGIN = 'check_login'
IS_VERIFIED = 'is_verified'
CHECK_VERIFID = 'check_verified'
IS_FINISHED = 'is_finished'
USER_DATA = 'user_data'
HTML = 'html'
EX1 = 'ex1'
EX2 = 'ex2'
EX3 = 'ex3'

# 队列
TASK_QUEUE = 'task_queue'


# 任务

# 登陆前:
PRE_LOGIN = 'pre_login'

# 登录
LOGING = 'loging'

# 验证

VERIFY = 'verify'