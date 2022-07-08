from typing import List, Tuple

from db.operation.sales import Sales
from db.standard import standard_update, standard_query

insertion_sales = "insert into 销售订单销量 (销售单号,蓝气罐销量,轻饮酒销量,填写日期,归属大区) " \
                  "values (%s,%s,%s,%s,%s)"
query_sales_record = "select * from 销售订单销量"
condition_sales_by_area_and_date = "where 填写日期 = %s and 归属大区 = %s"


def insert_sales(new_sales: Sales) -> bool:
    """
    将一条新的销量插入数据库中。会返回是否成功。

    :param new_sales: Sales 销量记录
    :return: bool
    """
    sql = insertion_sales
    return standard_update(sql, new_sales.generate_tuple())


def __query_sales(condition: str, params: Tuple = ()) -> List[Sales]:
    """
    根据给定条件查询单月销量，返回一个列表对象。
    Args:
        condition: : str 查询的条件（例如‘where attribute1 = xxx’）
        params: Tuple
    Returns:List[OneMonthPredict]
    """
    r = []
    sql = query_sales_record + " " + condition
    tuples = standard_query(sql, params)
    if tuples is None:
        raise ValueError("standard_query() returns None")
    for the_tuple in tuples:
        r.append(Sales(*the_tuple[1:], data_id=the_tuple[0]))
    return r


def query_reality_by_area(area: str, date: str) -> List[Sales]:
    """
    根据日期和大区，返回一个sales
    :param area: 地区
    :param date: 年月
    :return:
    """
    return __query_sales(condition_sales_by_area_and_date, (date, area))
