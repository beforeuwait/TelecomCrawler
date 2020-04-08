# coding=utf-8

import time
from . import TASK_QUEUE
from . import PRE_LOGIN
from . import calculate_md5
from . import hmset_data
from . import push_msg_2_queue


def generate_case_id(info: dict) -> None:
    # step1: 计算case_id
    case_id =  calculate_case_id(info.get('phone'))
    # step2: 存储信息到hash table里
    save_2_hash_table(case_id, info)
    # task_queue 第一个任务
    msg = {'case_id': case_id, 'task': PRE_LOGIN}
    psuh_msg_2_task_queue(msg)
    return case_id


def calculate_case_id(phone_number: str) -> str:
    return calculate_md5('_'.join([phone_number, str(int(1000*time.time()))]))


def save_2_hash_table(case_id: str, info: dict) -> None:
    hmset_data(id_key=case_id, data_dict=info)


def psuh_msg_2_task_queue(msg: dict):
    push_msg_2_queue(queue=TASK_QUEUE, msg=msg)