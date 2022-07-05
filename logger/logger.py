import logging
import traceback
from typing import Optional

# 设置2个可供其他包引用的logger类，分别用作不同的用途并写入不同的文件
# 是否打开日志；默认为是（在测试期间可以为否，其他时间都应该为是）
turn_on_logging = True

# 分界线，用于区分日志的不同部分
line_mark = "------------------------------------------------------------------------"


class __Logger:
    """
    自定义的日志类。
    """

    def __init__(self, logger_name: str, log_level: int, output_file: str):
        """
        自定义的日志类。

        :param logger_name: str 这个logger的名称，必须唯一
        :param log_level: int 日志等级（如logging.INFO）
        :param output_file: str 输出日志文件的路径
        """
        the_logger = logging.getLogger(logger_name)
        the_logger.setLevel(log_level)
        __handler = logging.FileHandler(output_file, encoding="UTF-8")
        __formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        __handler.setFormatter(__formatter)
        the_logger.addHandler(__handler)
        self.logger = the_logger
        self.default_level = log_level

    def log(self, msg, level: Optional[int] = None, enable_traceback: bool = False, line_below: bool = False):
        """
        记录日志。

        :param msg: Any
        :param level: int 默认为None，即使用日志类本身的级别。可以手动指定。
        :param enable_traceback: bool 是否显示traceback
        :param line_below: bool 是否在结尾处添加一条分界线
        :return: None
        """
        if level is None:
            level = self.default_level
        if enable_traceback:
            self.logger.log(level, traceback.format_exc())
        if turn_on_logging:
            self.logger.log(level, msg)
        if line_below:
            self.logger.log(level, line_mark)


# 清除根logger的handle使得我们的自定义logger可以正常运行
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# 两个用来给其他包引用的单例
infoLogger = __Logger("info_12345", logging.INFO, "log_info.txt")
errLogger = __Logger("err_12345", logging.ERROR, "log_err.txt")
bonusCalculationLog = __Logger("predict_cal_12345", logging.INFO, "log_predict.txt")
