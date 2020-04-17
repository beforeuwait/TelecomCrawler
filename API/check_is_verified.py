# coding=utf-8


from . import hget_name
from . import IS_VERIFIED
from . import api_log


def check_is_verified(case_id) -> bool:
    is_verified = hget_name(case_id, IS_VERIFIED)
    if not isinstance(is_verified, bool):
        api_log.warning('本次轮询，未查询到 {0} 的验证状态 {1}，请检查爬虫或者web未按照顺序请求'.format(case_id, is_verified))
        return False
    return is_verified