# coding=utf-8


from . import api_log
from . import calculate_run_time
from . import generate_case_id_push_2_task_queue
import tornado.web
from tornado.ioloop import IOLoop


class TCrawlerServer(tornado.web.RequestHandler):
    """
    接受post请求
    一共6个参数，对应不同的结果
    """
    param_names = [
        'user_info', 
        'login_code', 
        'verify_code', 
        'case_id', 
        'is_login', 
        'is_verified',
        'data']

    def get(self):
        self.write('welcome')
    
    def post(self):
        """
        接受参数
        验证参数
        选择方法
        """
        info = self.get_arguments('user_info')
        if info:
            case_id = self.do_generate_case_id(info)
            self.write(case_id)
            return

        case_id = self.get_argument('case_id')
        login_code = self.get_argument('login_code')
        if login_code and case_id:
            # 执行登录
            return
        
        is_login = self.get_argument('is_login')
        if case_id and is_login:
            # 验证登录是否成功
            return
        
        verify_code = self.get_argument('verify_code')
        if verify_code and case_id:
            # 详情页面登录
            return
        
        is_verified = self.get_argument('is_verified')
        if case_id and is_verified:
            # 验证详情页面是否验证成功
            return
        data = self.get_argument('data')
        if case_id and data:
            # 返回数据
            return

        
            
    
    @calculate_run_time
    def do_generate_case_id(self, info: dict) -> None:
        """计算case_id 然后丢入任务队列
        """
        generate_case_id_push_2_task_queue(info)


application = tornado.web.Application([(r"/TCrawler", TCrawlerServer),])

if __name__ == "__main__":
    application.listen(26000)
    IOLoop.instance().start()
