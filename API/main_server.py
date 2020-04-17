# coding=utf-8


from . import api_log
from . import calculate_run_time
from . import generate_case_id_push_2_task_queue
from . import receive_login_code_push_2_task_queue
from . import receive_verify_code_push_2_task_queue
from . import check_is_login
from . import check_is_verified
from . import check_is_finished
from . import get_user_data
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
        'check_login',
        'check_verified',
        'check_finished'
        'data']

    def get(self):
        self.write('welcome')
    
    def post(self):
        """
        接受参数
        验证参数
        选择方法
        """
        api_log.debug('__接收到任务')
        info = self.get_arguments('user_info')
        if info and isinstance(info, dict):
            api_log.debug('该任务为生成case_id, \t信息为{0}'.format(info))
            case_id = self.do_generate_case_id(info)
            self.write(case_id)
            return

        case_id = self.get_argument('case_id')
        login_code = self.get_argument('login_code')
        if login_code and case_id:
            # 执行登录
            api_log.debug('该任务为登录任务\t{0}\t{1}'.format(case_id, login_code))
            self.do_login(case_id, login_code)
            self.write('OK')
            return
        
        check_login = self.get_argument('check_login')
        if case_id and check_login:
            # 验证登录是否成功
            is_login = self.do_check_login(case_id)
            if is_login:
                self.write('1')
            else:
                self.write('0')
            return
        
        verify_code = self.get_argument('verify_code')
        if verify_code and case_id:
            # 详情页面登录
            self.do_verify(case_id, verify_code)
            self.write('OK')
            return
        
        check_verified = self.get_argument('check_verified')
        if case_id and check_verified:
            # 验证详情页面是否验证成功
            is_verified = self.do_check_is_verified(case_id)
            if is_verified:
                self.write('1')
            else:
                self.write('0')
            return

        check_finished = self.get_argument('check_finished')
        if case_id and check_finished:
            # 轮询是否已经采集完毕
            is_finished = self.do_check_is_finished(case_id)
            if is_finished:
                self.write('1')
            else:
                self.write('0')
            return
            
        data = self.get_argument('data')
        if case_id and data:
            # 返回数据
            user_data = self.do_get_user_data(case_id)
            self.write(user_data)
            return

    @calculate_run_time
    def do_generate_case_id(self, info: dict) -> str:
        """计算case_id 然后丢入任务队列
        """
        case_id = generate_case_id_push_2_task_queue(info)
        return case_id

    @calculate_run_time
    def do_login(self, case_id, login_code) -> None:
        """接受登录验证码，转发验证码并登录
        """
        receive_login_code_push_2_task_queue(case_id, login_code)
        return

    @calculate_run_time
    def do_check_login(self, case_id) -> bool:
        """属于web端轮询
        通过case_id来查询是否登录成功，前端好进行下一步
        """
        is_login = check_is_login(case_id)
        return is_login

    @calculate_run_time
    def do_verify(self, case_id, verify_code) -> None:
        """登录成功后，爬虫部分会去请求详情，然后开始验证
        这里接收到前端传来的验证码，并下发任务
        """
        receive_verify_code_push_2_task_queue(case_id, verify_code)
        return

    @calculate_run_time
    def do_check_is_verified(self, case_id) -> bool:
        """属于web端轮询
        通过case_id来查询是否验证成功
        """
        is_verifies = check_is_verified(case_id)
        return is_verifies

    @calculate_run_time
    def do_check_is_finished(self, case_id) -> bool:
        is_finished = check_is_finished(case_id)
        return is_finished

    @calculate_run_time
    def do_get_user_data(self, case_id) -> str:
        data = get_user_data(case_id)
        return data


application = tornado.web.Application([(r"/TCrawler", TCrawlerServer), ])

if __name__ == "__main__":
    application.listen(26000)
    IOLoop.instance().start()
