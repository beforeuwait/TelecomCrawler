# code=utf-8


from . import hget_name
from . import USER_DATA


def get_user_data(case_id) -> str:
    data = hget_name(case_id, USER_DATA)
    return data
