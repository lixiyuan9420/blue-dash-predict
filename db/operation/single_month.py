# 单月销量预测

from typing import Tuple


# create table 单月销量预测(
#         id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
#         预算制定流水号 varchar(50),
#         预算填写人 varchar(10),
#         预算期间 varchar(10),
#         预算部门 varchar(20),
#         预测销售总金额 float,
#         预计新增门店数 int,
#         线下渠道预估轻饮酒总销量（瓶） int,
#         线下渠道预估蓝气罐总销量（箱） int,
#         销售预测 varchar(20),
#         大区 varchar(20),
#         省份 varchar(20),
#         区域 varchar(255),
#         电商平台 varchar(20),
#         备注 varchar(200)
#     )

class OneMonthPredict:
    """
    单月预测表
    Attributes:
        predict_id:预算制定流水号
        predict_man: 预算填写人
        predict_start_time: 预算期间
        predict_part: 预算部门
        total_money_one:预测销售总金额
        increase_shops_one:预计新增门店数
        bottle_sale_one:线下渠道预估轻饮酒总销量（瓶）
        box_sale_one:线下渠道预估蓝气罐总销量（箱）
        predict_sale:销售预测
        area_one:大区-第一月线下
        province_one:省份-第一月线下
        region_one:区域-第一月线下
        platform:电商平台
        record:备注
        data_id: 这条记录在数据库里的id，通常不用, 默认-1
    """

    def __init__(self, predict_id: str, predict_man: str, predict_start_time: str,
                 predict_part: str, total_money_one: float, increase_shops_one: int, bottle_sale_one: int,
                 box_sale_one: int, predict_sale: float, area_one: str, province_one: str, region_one: str,
                 platform: str, record: str, data_id: int = -1):
        """

        :param predict_id: 预算制定流水号
        :param predict_man: 预算填写人
        :param predict_start_time: 预算期间
        :param predict_part: 预算部门
        :param total_money_one: 预测销售总金额
        :param increase_shops_one: 预计新增门店数
        :param bottle_sale_one: 线下渠道预估轻饮酒总销量
        :param box_sale_one: 线下渠道预估蓝气罐总销量
        :param predict_sale: 销售预测
        :param area_one: 大区-第一月线下
        :param province_one: 省份-第一月线下
        :param region_one: 区域-第一月线下
        :param platform: 电商平台
        :param record: 备注
        :param data_id: 这条记录在数据库里的id，通常不用, 默认-1
        """
        self.predict_id = predict_id
        self.predict_man = predict_man
        self.predict_start_time = predict_start_time
        self.predict_part = predict_part
        self.total_money_one = total_money_one
        self.increase_shops_one = increase_shops_one
        self.bottle_sale_one = bottle_sale_one
        self.box_sale_one = box_sale_one
        self.predict_sale = predict_sale
        self.area_one = area_one
        self.province_one = province_one
        self.region_one = region_one
        self.platform = platform
        self.record = record
        self.data_id = data_id

    def generate_tuple(self) -> Tuple:
        """
            返回一个用于插入新记录的有序元组。
        """
        return (self.predict_id, self.predict_man, self.predict_start_time, self.predict_part,
                self.total_money_one, self.increase_shops_one, self.bottle_sale_one, self.box_sale_one,
                self.predict_sale, self.area_one, self.province_one, self.region_one, self.platform, self.record)
