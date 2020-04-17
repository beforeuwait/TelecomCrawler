# coding=utf-8

from . import hget_name
from . import IS_LOGIN
from . import api_log


def check_is_login(case_id) -> bool:
    # 直接读取hash_table 里
    is_login = hget_name(case_id, IS_LOGIN)
    if not isinstance(is_login, bool):
        api_log.warning('本次轮询，未查询到 {0} 的登录状态 {1}，请检查爬虫或者web未按照顺序请求'.format(case_id, is_login))
        return False
    return is_login
