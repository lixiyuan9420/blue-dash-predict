# flask
import flask.wrappers
from flask import (
    Blueprint, request
)
from flask_cors import CORS

# log
from db.operation import third_month_sql, single_month_sql, sales_sql
from logger.logger import infoLogger, errLogger
# request and response handler
from util.request_handler import use
from util.request_handler.common import verify_auth_token
from util.request_handler.sales import extract_sales
from util.request_handler.single_month import extract_single_month, verified_predict, __extract_predict_query
from util.request_handler.single_month_three import extract_single_month_three
from util.request_handler.single_month_two import extract_single_month_two
from util.request_handler.three_month import extract_third_month
from util.response_handler import response_success, response_failure, response_with_msg

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
        new_predict_three = extract_third_month(request.get_json())
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

    :return: flask.wrappers.Response
    """
    try:
        infoLogger.log("/predict/new_one_month 开始")
        new_predict_one = extract_single_month(request.get_json())
        success = single_month_sql.insert_single_month(new_predict_one)
        infoLogger.log("/predict/new_one_month success: " + str(success), line_below=True)
        return __quick_response(success)
    except Exception as e:
        __log_err(e, request)
        return response_failure()


@bp.route("/predict/new_one_month_two", methods=["POST"])
def new_one_month_two() -> flask.wrappers.Response:
    """
    插入一个新的一月销量预测,缓存第二月的数据。

    :return: flask.wrappers.Response
    """
    try:
        infoLogger.log("/predict/new_one_month_two 开始")
        new_predict_two = extract_single_month_two(request.get_json())
        success = single_month_sql.insert_single_month_two(new_predict_two)
        infoLogger.log("/predict/new_one_month_two success: " + str(success), line_below=True)
        return __quick_response(success)
    except Exception as e:
        __log_err(e, request)
        return response_failure()


@bp.route("/predict/new_one_month_three", methods=["POST"])
def new_one_month_three() -> flask.wrappers.Response:
    """
    插入一个新的一月销量预测,缓存第二月的数据。

    :return: flask.wrappers.Response
    """
    try:
        infoLogger.log("/predict/new_one_month_three 开始")
        new_predict_three = extract_single_month_three(request.get_json())
        success = single_month_sql.insert_single_month_three(new_predict_three)
        infoLogger.log("/predict/new_one_month_three success: " + str(success), line_below=True)
        return __quick_response(success)
    except Exception as e:
        __log_err(e, request)
        return response_failure()


@bp.route("/predict/new_sales", methods=["POST"])
def new_sales() -> flask.wrappers.Response:
    """
    插入一条新的销售记录，每成交一笔，就会存储销量到数据库中
    :return: flask.wrappers.Response
    """
    try:
        infoLogger.log("/predict/new_sales 开始")
        new_sales_one = extract_sales(request.get_json())
        success = sales_sql.insert_sales(new_sales_one)
        infoLogger.log("/predict/new_sales success: " + str(success), line_below=True)
        return __quick_response(success)
    except Exception as e:
        __log_err(e, request)
        return response_failure()


@bp.route("/predict/compute", methods=["POST"])
def new_sales_com() -> flask.wrappers.Response:
    """
    插入一条新的销售记录，每成交一笔，就会存储销量到数据库中
    :return: flask.wrappers.Response
    """
    try:
        infoLogger.log("/predict/compute 开始")

    except Exception as e:
        __log_err(e, request)
        return response_failure()


@bp.route("/predict/search_predict", methods=["POST"])
def search_predict() -> flask.wrappers.Response:
    """
    查询某年月的某大区的销售预测
    :return: flask.wrappers.Response
    """
    try:
        infoLogger.log("/predict/search_predict 开始")
        infoLogger.log(request)
        infoLogger.log(request.get_json())
        the_tuple = __extract_predict_query(request.get_json())
        msg = use.stringify_predict_records(*the_tuple)
        infoLogger.log("/predict/search_predict result: " + msg)
        return response_with_msg(msg)
    except Exception as e:
        __log_err(e, request)
        return response_failure()
