# coding=utf-8

from . import push_msg_2_queue
from . import TASK_QUEUE
from . import LOGING
from . import hset_name
from . import LOGIN_CODE


def receive_login_code_push_2_task_queue(case_id: str, login_code: str) -> None:
    # 把login_code写入hash_table
    # 这里有个问题，就是被注入
    # 这里为了安全可以单独给个队列来验证写入
    hset_name(id_key=case_id, field=LOGIN_CODE, value=login_code)
    # 创建任务
    msg = {'case_id': case_id, 'task': LOGING}
    # 派发任务
    push_msg_2_queue(TASK_QUEUE, msg)
    return
