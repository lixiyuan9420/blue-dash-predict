from db.operation.single_month import OneMonthPredict
from util.request_handler.common import convert_to_int, convert_to_float, verify_auth_token


def __extract_single_month(data_json) -> OneMonthPredict:
    """
    从JSON结构体中抽取出一个单月销量的预测。
    JSON结构体应该格式如下：
    e.g., {"单月销量预测": {

        '预算制定流水号':"xxx"
        '预算填写人':"xxx"
        '预算期间':"xxx"
        '预算部门':"xxx"
        '预测销售总金额':1000.00
        '预计新增门店数':30
        '线下渠道预估轻饮酒总销量（瓶）':50
        '线下渠道预估蓝气罐总销量（箱）':50
        '销售预测':"xxx"
        '大区':"xxx"
        '省份':"xxx"
        '区域':"xxx"
        '电商平台':"xxx"
        '备注':"xxx"}
    }
    :param data_json: JSON
    :return:OneMonthPredict
    """
    data = data_json["单月销量预测"]
    predict_id = data["预算制定流水号"]
    predict_man = data["预算填写人"]
    predict_start_time = data["预算期间"]
    predict_part = data["预算部门"]
    total_money_one = convert_to_float(data["预测销售总金额"])
    increase_shops_one = convert_to_int(data["预计新增门店数"])
    bottle_sale_one = convert_to_int(data["线下渠道预估轻饮酒总销量（瓶）"])
    box_sale_one = convert_to_int(data["线下渠道预估蓝气罐总销量（箱）"])
    predict_sale = data["销售预测"]
    area_one = data["大区"]
    province_one = data["省份"]
    region_one = data["区域"]
    platform = data["电商平台"]
    record = data["备注"]
    date = data["填写日期"]
    return OneMonthPredict(predict_id, predict_man, predict_start_time, predict_part, total_money_one,
                           increase_shops_one,
                           bottle_sale_one, box_sale_one, predict_sale, area_one, province_one, region_one, platform,
                           record, date)


def verified_single_month(data_json) -> OneMonthPredict:
    """
    验证请求身份，并从JSON结构体中抽取出一个单月销量预测。
    JSON结构体应该格式如下：
    e.g., {
        "单月销量预测": {

            '预算制定流水号':"xxx"
            '预算填写人':"xxx"
            '预算期间':"xxx"
            '预算部门':"xxx"
            '预测销售总金额':1000.00
            '预计新增门店数':30
            '线下渠道预估轻饮酒总销量（瓶）':50
            '线下渠道预估蓝气罐总销量（箱）':50
            '销售预测':"xxx"
            '大区':"xxx"
            '省份':"xxx"
            '区域':"xxx"
            '电商平台':"xxx"
            '备注':"xxx"
        }
        "token": "abcdefg123"
    }

    :param data_json: JSON
    :return:OneMonthPredict
    """
    if verify_auth_token(data_json):
        return __extract_single_month(data_json)
    raise ValueError("验证身份信息失败！")
