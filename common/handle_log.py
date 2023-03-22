import logging
import mypath
from common.handle_conf_file import cf


class HandlerLog(logging.Logger):
    def __init__(self, log_name, lever, file_ok):
        log_name = log_name
        lever = lever
        file_ok = file_ok
        fmt = '%(asctime)s:%(name)s:%(funcName)s:%(filename)s:%(lineno)d:%(levelname)s:%(message)s'
        super().__init__(log_name, lever)

        # 创建收集器
        logger = logging.getLogger(log_name)

        # 设置收集器级别
        logger.setLevel(lever)

        # 创建渠道
        console = logging.StreamHandler()

        # 设置日志格式
        formate = logging.Formatter(fmt)

        # 渠道绑定格式
        console.setFormatter(formate)

        # 收集器绑定渠道
        self.addHandler(console)

        if file_ok:
            # 创建文件渠道
            file_handel = logging.FileHandler(mypath.log_file_dir + r'\{}.log'.format('new_log'), mode='w',
                                              encoding='utf-8')
            file_handel.setLevel(lever)
            file_handel.setFormatter(formate)
            self.addHandler(file_handel)


log = HandlerLog(cf.get_str('Log', 'name'), cf.get_str('Log', 'level'), cf.get_str('Log', 'file_ok'))
if __name__ == '__main__':
    log = HandlerLog(cf.get_str('Log', 'name'), cf.get_str('Log', 'level'), cf.get_str('Log', 'file_ok'))
    log.info('11111111111111')
