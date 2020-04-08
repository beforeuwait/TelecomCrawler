# coding=utf-8


import os
import time
import logging


# logging模块
api_log = logging.getLogger(name='TelecomCrawlerAPI')
api_log.setLevel(logging.DEBUG)
handler = logging.FileHandler(os.path.join(os.path.split(__file__)[0], './TCrawlerAPI.log'))
fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(fmt)
api_log.addHandler(handler)
