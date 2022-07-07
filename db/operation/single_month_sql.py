# 单月预测

from typing import List, Tuple

from db.operation.single_month import OneMonthPredict
from db.standard import standard_update, standard_query

insertion_single_month = "insert into 单月销量预测(预算制定流水号,预算填写人,预算期间,预算部门,预测销售总金额,预计新增门店数," \
                         "`线下渠道预估轻饮酒总销量（瓶）`,`线下渠道预估蓝气罐总销量（箱）`,`电商预估轻饮酒总销量（瓶）`," \
                         "`电商预估蓝气罐总销量（箱）`,销售预测,大区,省份,区域,电商平台,备注,填写日期)" \
                         "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
insertion_single_month_two = "insert into 单月销量预测第二月(预算制定流水号,预算填写人,预算期间,预算部门,预测销售总金额,预计新增门店数," \
                         "`线下渠道预估轻饮酒总销量（瓶）`,`线下渠道预估蓝气罐总销量（箱）`,`电商预估轻饮酒总销量（瓶）`," \
                         "`电商预估蓝气罐总销量（箱）`,销售预测,大区,省份,区域,电商平台,备注,填写日期)" \
                         "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
insertion_single_month_three = "insert into 单月销量预测第三月(预算制定流水号,预算填写人,预算期间,预算部门,预测销售总金额,预计新增门店数," \
                         "`线下渠道预估轻饮酒总销量（瓶）`,`线下渠道预估蓝气罐总销量（箱）`,`电商预估轻饮酒总销量（瓶）`," \
                         "`电商预估蓝气罐总销量（箱）`,销售预测,大区,省份,区域,电商平台,备注,填写日期)" \
                         "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
query_single_month = "select * from 单月销量预测"
update_single_month = "update 单月销量预测 set 预测销售总金额 = %s, 预计新增门店数 = %s ,`线下渠道预估轻饮酒总销量（瓶）` = %s," \
                      "`线下渠道预估蓝气罐总销量（箱）` = %s where 预算填写人 = %s and 预算期间 = %s"
condition_total_by_area = "where 大区 = %s and 填写日期 = %s"


def insert_single_month(single_month: OneMonthPredict) -> bool:
    """
    将一条新的单月销量预测插入数据库中。会返回是否成功。

    :param single_month: OneMonthPredict 经销商合同
    :return: bool
    """
    sql = insertion_single_month
    return standard_update(sql, single_month.generate_tuple())


def insert_single_month_two(single_month: OneMonthPredict) -> bool:
    """
    将一条新的单月销量预测插入数据库中。会返回是否成功。

    :param single_month: OneMonthPredict 经销商合同
    :return: bool
    """
    sql = insertion_single_month_two
    return standard_update(sql, single_month.generate_tuple())


def insert_single_month_three(single_month: OneMonthPredict) -> bool:
    """
    将一条新的单月销量预测插入数据库中。会返回是否成功。

    :param single_month: OneMonthPredict 经销商合同
    :return: bool
    """
    sql = insertion_single_month_three
    return standard_update(sql, single_month.generate_tuple())


def __query_single_month(condition: str, params: Tuple = ()) -> List[OneMonthPredict]:
    """
    根据给定条件查询单月销量预测，返回一个列表对象。
    Args:
        condition: : str 查询的条件（例如‘where attribute1 = xxx’）
        params: Tuple
    Returns:List[OneMonthPredict]
    """
    r = []
    sql = query_single_month + " " + condition
    tuples = standard_query(sql, params)
    if tuples is None:
        raise ValueError("standard_query() returns None")
    for the_tuple in tuples:
        r.append(OneMonthPredict(*the_tuple[1:], data_id=the_tuple[0]))
    return r


def query_total_by_area(area: str, date: str) -> List[OneMonthPredict]:
    """


    :param date: str
    :param area: str
    :return: List[OneMonthPredict] 理论上长度应该等于1
    """

    return __query_single_month(condition_total_by_area, (area, date))


def __update_single_month(params: Tuple = ()) -> bool:
    """
    根据给定条件更新单月的销量预测
    :param params: Tuple
    :return: List[OneMonthPredict]
    """
    sql = update_single_month
    return standard_update(sql, params)
