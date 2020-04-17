# coding=utf-8

from . import hget_name
from . import IS_FINISHED
from . import api_log


def check_is_finished(case_id) -> bool:
    is_finished = hget_name(case_id, IS_FINISHED)
    if not isinstance(is_finished, bool):
        api_log.warning('本次轮询，未查询到 {0} 是否爬取完毕 {1}，请检查爬虫或者web未按照顺序请求'.format(case_id, is_finished))
        return False
    return is_finished