from typing import Optional, List

from db.operation.sales import Sales
from db.operation.sales_sql import query_reality_by_area
from db.operation.single_month import OneMonthPredict
from db.operation.single_month_sql import query_by_area
from logger.logger import errLogger


def __search_predict_records(region: Optional[str], year_month: Optional[str]) -> List[OneMonthPredict]:
    """
    查询预测销量
    :param region:
    :param year_month:
    :return:
    """
    return query_by_area(region, year_month)


def __search_reality_records(region: Optional[str], year_month: Optional[str]) -> List[Sales]:
    """
    查询实际销量
    :param region:
    :param year_month:
    :return:
    """
    return query_reality_by_area(region, year_month)


def stringify_predict_records(region: Optional[str], year_month: Optional[str]) -> str:
    """
    搜索某一年月，某一大区的预估记录。

    :param year_month: 年月
    :param region: 大区
    :return: str
    """
    try:
        records = __search_predict_records(region, year_month)
        s = ''
        total_box = 0.0
        total_bottle = 0.0
        if len(records) == 0:
            return "该记录暂时还未计算，等下一个月"

        for record in records:
            s = s + "大区: " + str(record.area_one) + \
                " 预估线下蓝气罐：" + str(record.box_sale_one) + \
                " 预估线下轻饮酒: " + str(record.bottle_sale_one) + \
                " 预估线上蓝气罐：" + str(record.online_box) + \
                " 预估线上轻饮酒: " + str(record.online_bottle) + \
                " 时间： " + str(record.date) + "\n"
            total_box = total_box + record.box_sale_one + record.online_box
            total_bottle = total_bottle + record.bottle_sale_one + record.online_bottle
        return s + "蓝气罐总销量：" + str(total_box) + "轻饮酒总销量：" + str(total_bottle)
    except AssertionError as e:
        return str(e)
    except Exception as e:
        errLogger.log(e, enable_traceback=True, line_below=True)
        return str(e)


def stringify_reality_records(region: Optional[str], year_month: Optional[str]) -> str:
    """
    搜索某一年月，某一大区的实际销量记录。

    :param year_month: 年月
    :param region: 大区
    :return: str
    """
    try:
        records = __search_reality_records(region, year_month)
        s = ''
        total_box = 0.0
        total_bottle = 0.0
        if len(records) == 0:
            return "该记录暂时还未计算，等下一个月"

        for record in records:
            s = s + "大区: " + str(record.area) + \
                " 蓝气罐：" + str(record.box_sale) + \
                " 轻饮酒: " + str(record.bottle_sale) + \
                " 时间： " + str(record.date) + "\n"
            total_box = total_box + record.box_sale
            total_bottle = total_bottle + record.bottle_sale
        return s + "实际蓝气罐总销量：" + str(total_box) + "实际轻饮酒总销量：" + str(total_bottle)
    except AssertionError as e:
        return str(e)
    except Exception as e:
        errLogger.log(e, enable_traceback=True, line_below=True)
        return str(e)


def compute(region: Optional[str], year_month: Optional[str]) -> str:
    global record
    reality_records = __search_reality_records(region, year_month)
    predict_records = __search_predict_records(region, year_month)
    reality_records_total_box = 0.0
    reality_records_total_bottle = 0.0
    predict_records_total_box = 0.0
    predict_records_total_bottle = 0.0
    achievement = 0
    bottle_achievement = 0
    for record in reality_records:
        reality_records_total_box = reality_records_total_box + record.box_sale
        reality_records_total_bottle = reality_records_total_bottle + record.bottle_sale

    for record in predict_records:
        predict_records_total_box = predict_records_total_box + record.box_sale_one + record.online_box
        predict_records_total_bottle = predict_records_total_bottle + record.bottle_sale_one + record.online_bottle

    balance = reality_records_total_box - predict_records_total_box
    bottle_balance = reality_records_total_bottle - predict_records_total_bottle
    if reality_records_total_box != 0:
        achievement = predict_records_total_box / reality_records_total_box * 100
    if reality_records_total_bottle != 0:
        bottle_achievement = predict_records_total_bottle / reality_records_total_bottle * 100
    return "蓝气罐差额  |" + "达成率  |" +"轻饮酒差额 |" + "达成率 |\n" \
           + str(balance) + "    |" + str(achievement) + "%  |" + str(bottle_balance) + "     |" + str(bottle_achievement) + "% |"
