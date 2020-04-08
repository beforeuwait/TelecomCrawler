# coding=utf-8


from . import api_log
from . import calculate_run_time
from . import generate_case_id_push_2_task_queue
import tornado.web
from importlib import reload
from tornado.ioloop import IOLoop


class TCrawlerServer(tornado.web.RequestHandler):
    """
    接受post请求
    这里不对参数做校验，默认正确的
    """
    param_names = ['', '', '']

    def get(self):
        self.write('welcome')
    
    def post(self):
        # todo: 唯一入口
        pass
    
    @calculate_run_time
    def do_generate_case_id(self, info):
        """计算case_id 然后丢入任务队列
        """
        generate_case_id_push_2_task_queue(info)


application = tornado.web.Application([(r"/TCrawler", TCrawlerServer),])

if __name__ == "__main__":
    application.listen(26000)
    IOLoop.instance().start()
