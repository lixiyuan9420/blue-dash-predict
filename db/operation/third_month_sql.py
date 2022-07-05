# 三月预测

from typing import List, Tuple

from db.operation.third_month import ThirdMonthPredict
from db.standard import standard_update, standard_query

insertion_three_month = "insert into 三月销量预测(预算制定流水号,预算填写人,预算期间," \
                        "预算截止期,预算部门,预测销售总金额,预计新增门店数,`线下渠道预估轻饮酒总销量（瓶）`," \
                        "`线下渠道预估蓝气罐总销量（箱）`,`预测销售总金额-二月`,`预计新增门店数-二月`,`线下渠道预估轻饮酒总销量（瓶）-二月`," \
                        "`线下渠道预估蓝气罐总销量（箱）-二月`,`预测销售总金额-三月`,`预计新增门店数-三月`,`线下渠道预估轻饮酒总销量（瓶）-三月`," \
                        "`线下渠道预估蓝气罐总销量（箱）-三月`,销售预测,`大区-第一月线下`,`省份-第一月线下`,`区域-第一月线下`,`大区-第二月线下`," \
                        "`省份-第二月线下`,`区域-第二月线下`,`大区-第三月线下`,`省份-第三月线下`,`区域-第三月线下`,电商平台,备注,`预测销售总金额（三个月）`)" \
                        "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
query_three_month = "select * from 三月销量预测"

# 用于计算判断
condition_ = "where "


def insert_third_month(single_month: ThirdMonthPredict) -> bool:
    """
    将一条新的单月销量预测插入数据库中。会返回是否成功。

    :param single_month: OneMonthPredict 经销商合同
    :return: bool
    """
    sql = insertion_three_month
    return standard_update(sql, single_month.generate_tuple())


def __query_single_month(condition: str, params: Tuple = ()) -> List[ThirdMonthPredict]:
    """
    根据给定条件查询单月销量预测，返回一个列表对象。
    Args:
        condition: : str 查询的条件（例如‘where attribute1 = xxx’）
        params: Tuple
    Returns:List[OneMonthPredict]
    """
    r = []
    sql = query_three_month + " " + condition
    tuples = standard_query(sql, params)
    if tuples is None:
        raise ValueError("standard_query() returns None")
    for the_tuple in tuples:
        r.append(ThirdMonthPredict(*the_tuple[1:], data_id=the_tuple[0]))
    return r
