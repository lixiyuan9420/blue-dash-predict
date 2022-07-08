# 实际销量


# create table 销售订单销量(
#         id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
#         销售单号 varchar(200),
#         蓝气罐销量 int,
#         轻饮酒销量 int,
#         填写日期 int,
#         归属大区 varchar(50)
#     )
from typing import Tuple


class Sales:
    """
    销售订单销量
    Attributes:
        sales_id: 销售单号
        box_sale: 蓝气罐销量
        bottle_sale: 轻饮酒销量
        date: 填写日期
        area: 归属大区
    """

    def __init__(self, sales_id: str, box_sale: int, bottle_sale: int, date: int, area: str, data_id: int = -1):
        """

        :param sales_id: 销售单号
        :param box_sale: 蓝气罐销量
        :param bottle_sale: 轻饮酒销量
        :param date: 填写日期
        :param area: 归属大区
        :param data_id: 这条记录在数据库里的id，通常不用, 默认-1

        """
        self.sales_id = sales_id
        self.box_sale = box_sale
        self.bottle_sale = bottle_sale
        self.date = date
        self.area = area
        self.data_id = data_id

    def generate_tuple(self) -> Tuple:
        """
        返回一个用于插入新记录的有序元组。
        (销售单号,蓝气罐销量,轻饮酒销量,填写日期,归属大区)
        :return: Tuple
        """
        return (self.sales_id, self.box_sale, self.bottle_sale,
                self.date, self.area)
