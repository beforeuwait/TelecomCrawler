# coding=utf-8

import time
from . import calculate_md5
from . import hmset_data


def generate_case_id(info):
    # step1: 计算case_id
    case_id =  calculate_case_id(info.get('phone'))
    # step2: 存储信息到hash table里
    save_2_hash_table(case_id, info)
    # task_queue 第一个任务



def calculate_case_id(phone_number):
    return calculate_md5('_'.join([phone_number, str(int(1000*time.time()))]))


def save_2_hash_table(case_id, info):
    hmset_data(id_key=case_id, data_dict=info)