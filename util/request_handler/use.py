from typing import Optional, List

from db.operation.single_month import OneMonthPredict
from db.operation.single_month_sql import query_by_area
from logger.logger import errLogger


def __search_predict_records(region: Optional[str], year_month: Optional[str]) -> List[OneMonthPredict]:
    return query_by_area(region, year_month)


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
