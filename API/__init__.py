# coding=utf-8

"""
该模块为 API 模块，同 client 通信

check_is_login.py: client轮询case_id状态，返回是否登陆成功
check_is_verified.py: client轮询case_id状态，返回是否验证成功
generate_case_id.py: 返回api接收到的 md5(手机号 + 时间戳)作为当前的事件id(case_id),然后丢入任务队列，开始预登陆操作
main_server.py: 对外api
receive_login_code.py: 处理登录短信验证码，然后丢入任务队列(登录任务)
receive_verify_code.py: 处理详情查询短信验证码，然后丢入任务队列(验证任务)
get_data.py: client轮询该case_id，返回查询到的数据
utils.py: 工具

接受参数,部分字段调整

{
    'phone': '18200120031',
    'name': '',
    'pwd': '112233',
    'card': '511324199012120034',
    'cookies': '',
    'captcha': '',
    'login_code': '',
    'verify_code': '',
    'telecom': '',
    'info': '',
    'is_login': '',
    'is_verify': '',
    'html': '',
    'ex1': '',
    'ex2': '',
    'ex3': '',
    'ex4': '',
    'data': ''
    }
"""

__all__ = ['']

from .utils import api_log
from .generate_case_id import generate_case_id as generate_case_id_push_2_task_queue
from utils import hmset_data
from utils import push_msg_2_queue
from utils import calculate_md5
from utils import calculate_function_run_time_ms_for_API as calculate_run_time
from config import TASK_QUEUE
from config import PRE_LOGIN

