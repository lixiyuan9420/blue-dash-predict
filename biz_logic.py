# flask
import flask.wrappers
from flask import (
    Blueprint, request
)
from flask_cors import CORS

# log
from db.operation import third_month_sql, single_month_sql
from logger.logger import infoLogger, errLogger

# request and response handler
from util.request_handler.common import verify_auth_token
from util.request_handler.single_month import verified_single_month
from util.request_handler.three_month import verified_third_month

from util.response_handler import response_success, response_failure

# db operation


# 创建一个蓝图
bp = Blueprint('biz_logic', __name__)
# 允许跨域请求
cors = CORS(bp)


def __log_err(e: Exception, req: request):
    """
    在发生错误时将错误写入日志中

    :param e:Exception
    :param req:request
    :return:None
    """
    errLogger.log("request:")
    errLogger.log(req)
    errLogger.log(e, enable_traceback=True, line_below=True)


def __quick_response(success: bool) -> flask.wrappers.Response:
    """
    回复最简单的成功或失败。

    :param success: bool
    :return: flask.wrappers.Response:
    """
    if success:
        return response_success()
    else:
        return response_failure()


@bp.route("/mock_verification", methods=["POST"])
def mock_verification() -> flask.wrappers.Response:
    """
    一个虚假的路径，用来模拟身份验证。

    :return: flask.wrappers.Response
    """
    try:
        infoLogger.log("/mock_verification 开始")
        verify_auth_token(request.get_json())
        response = response_success()
        infoLogger.log("/mock_verification 完成", line_below=True)
        return response
    except Exception as e:
        __log_err(e, request)
        return response_failure()


@bp.route("/predict/new_three_month", methods=["POST"])
def new_three_month() -> flask.wrappers.Response:
    """
    插入一个新的三月销量预测。

    :return: flask.wrappers.Response:
    """
    try:
        infoLogger.log("/predict/new_three_month 开始")
        new_predict_three = verified_third_month(request.get_json())
        success = third_month_sql.insert_third_month(new_predict_three)
        infoLogger.log("/predict/new_three_month success: " + str(success), line_below=True)
        return __quick_response(success)
    except Exception as e:
        __log_err(e, request)
        return response_failure()


@bp.route("/predict/new_one_month", methods=["POST"])
def new_one_month() -> flask.wrappers.Response:
    """
    插入一个新的一月销量预测。

    :return: flask.wrappers.Response:
    """
    try:
        infoLogger.log("/predict/new_one_month 开始")
        infoLogger.log(request.get_json())
        new_predict_one = verified_single_month(request.get_json())
        success = single_month_sql.insert_single_month(new_predict_one)
        infoLogger.log("/predict/new_one_month success: " + str(success), line_below=True)
        return __quick_response(success)
    except Exception as e:
        __log_err(e, request)
        return response_failure()
