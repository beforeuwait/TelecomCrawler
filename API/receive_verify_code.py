# coding=utf-8

from . import hset_name
from . import VERIFY
from . import VERIFY_CODE
from . import TASK_QUEUE
from . import push_msg_2_queue


def receive_verify_code_push_2_task_queue(case_id, verify_code) -> None:
    # 把verify_code写入hash_table
    hset_name(case_id, field=VERIFY_CODE, value=verify_code)
    msg = {'case_id': case_id, 'task': VERIFY}
    push_msg_2_queue(TASK_QUEUE, msg)
    return