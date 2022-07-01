# 三月销量预测

from db.operation.third_month import ThirdMonthPredict
from util.request_handler.common import convert_to_float, convert_to_int, verify_auth_token


def __extract_third_month(data_json) -> ThirdMonthPredict:
    """
    从JSON结构体中抽取出一个单月销量的预测。
    JSON结构体应该格式如下：
    e.g., {"单月销量预测": {

        '预算制定流水号':"xxx"
        '预算填写人':"xxx"
        '预算期间':"xxx"
        '预算截止期':"xxx"
        '预算部门':"xxx"
        '预测销售总金额':1000.00
        '预计新增门店数':30
        '线下渠道预估轻饮酒总销量（瓶）':50
        '线下渠道预估蓝气罐总销量（箱）':50
        '预测销售总金额-二月':1000.00
        '预计新增门店数-二月':30
        '线下渠道预估轻饮酒总销量（瓶）-二月':50
        '线下渠道预估蓝气罐总销量（箱）-二月':50
        '预测销售总金额-三月':1000.00
        '预计新增门店数-三月':30
        '线下渠道预估轻饮酒总销量（瓶）-三月':50
        '线下渠道预估蓝气罐总销量（箱）-三月':50
        '销售预测':"xxx"
        '大区-第一月线下':"xxx"
        '省份-第一月线下':"xxx"
        '区域-第一月线下':"xxx"
        '大区-第二月线下':"xxx"
        '省份-第二月线下':"xxx"
        '区域-第二月线下':"xxx"
        '大区-第三月线下':"xxx"
        '省份-第三月线下':"xxx"
        '区域-第三月线下':"xxx"
        '电商平台':"xxx"
        '备注':"xxx"
        '预测销售总金额（三个月）':1000.00}
        "token": "abcdefg123"
    }
    :param data_json: JSON
    :return:ThirdMonthPredict
    """
    data = data_json["单月销量预测"]
    predict_id = data["预算制定流水号"]
    predict_man = data["预算填写人"]
    predict_start_time = data["预算期间"]
    predict_end_time = data["预算截止期"]
    predict_part = data["预算部门"]
    total_money_one = convert_to_float(data["预测销售总金额"])
    increase_shops_one = convert_to_int(data["预计新增门店数"])
    bottle_sale_one = convert_to_int(data["线下渠道预估轻饮酒总销量（瓶）"])
    box_sale_one = convert_to_int(data["线下渠道预估蓝气罐总销量（箱）"])
    total_money_two = convert_to_float(data["预测销售总金额-二月"])
    increase_shops_two = convert_to_int(data["预计新增门店数-二月"])
    bottle_sale_two = convert_to_int(data["线下渠道预估轻饮酒总销量（瓶）-二月"])
    box_sale_two = convert_to_int(data["线下渠道预估蓝气罐总销量（箱）-二月"])
    total_money_three = convert_to_float(data["预测销售总金额-三月"])
    increase_shops_three = convert_to_int(data["预计新增门店数-三月"])
    bottle_sale_three = convert_to_int(data["线下渠道预估轻饮酒总销量（瓶）-三月"])
    box_sale_three = convert_to_int(data["线下渠道预估蓝气罐总销量（箱）-三月"])
    predict_sale = data["销售预测"]
    area_one = data["大区-第一月线下"]
    province_one = data["省份-第一月线下"]
    region_one = data["区域-第一月线下"]
    area_two = data["大区-第二月线下"]
    province_two = data["省份-第二月线下"]
    region_two = data["区域-第二月线下"]
    area_three = data["大区-第三月线下"]
    province_three = data["省份-第三月线下"]
    region_three = data["区域-第三月线下"]
    platform = data["电商平台"]
    record = data["备注"]
    total_money_all = data["预测销售总金额（三个月）"]
    return ThirdMonthPredict(predict_id, predict_man, predict_start_time,predict_end_time, predict_part, total_money_one,
                             increase_shops_one, bottle_sale_one, box_sale_one, total_money_two, increase_shops_two,
                             bottle_sale_two, box_sale_two, total_money_three, increase_shops_three, bottle_sale_three,
                             box_sale_three, predict_sale, area_one, province_one, region_one, area_two, province_two,
                             region_two, area_three, province_three, region_three, platform, record, total_money_all)


def verified_third_month(data_json) -> ThirdMonthPredict:
    """
    验证请求身份，并从JSON结构体中抽取出一个三月销量预测。
    JSON结构体应该格式如下：
    e.g., {
        "三月销量预测": {

        '预算制定流水号':"xxx"
        '预算填写人':"xxx"
        '预算期间':"xxx"
        '预算截止期':"xxx"
        '预算部门':"xxx"
        '预测销售总金额':1000.00
        '预计新增门店数':30
        '线下渠道预估轻饮酒总销量（瓶）':50
        '线下渠道预估蓝气罐总销量（箱）':50
        '预测销售总金额-二月':1000.00
        '预计新增门店数-二月':30
        '线下渠道预估轻饮酒总销量（瓶）-二月':50
        '线下渠道预估蓝气罐总销量（箱）-二月':50
        '预测销售总金额-三月':1000.00
        '预计新增门店数-三月':30
        '线下渠道预估轻饮酒总销量（瓶）-三月':50
        '线下渠道预估蓝气罐总销量（箱）-三月':50
        '销售预测':"xxx"
        '大区-第一月线下':"xxx"
        '省份-第一月线下':"xxx"
        '区域-第一月线下':"xxx"
        '大区-第二月线下':"xxx"
        '省份-第二月线下':"xxx"
        '区域-第二月线下':"xxx"
        '大区-第三月线下':"xxx"
        '省份-第三月线下':"xxx"
        '区域-第三月线下':"xxx"
        '电商平台':"xxx"
        '备注':"xxx"
        '预测销售总金额（三个月）':1000.00
        }
        "token": "abcdefg123"
    }

    :param data_json: JSON
    :return:OneMonthPredict
    """
    if verify_auth_token(data_json):
        return __extract_third_month(data_json)
    raise ValueError("验证身份信息失败！")
