# 三个月的销量预测

from typing import Tuple


# 三个月的销量预测
# 数据唯一
# create table 三月销量预测 (
#        id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
#        预算制定流水号 varchar(50),
#        预算填写人 varchar(10),
#        预算期间 varchar(10),
#        预算截止期 varchar(10),
#        预算部门 varchar(20),
#        预测销售总金额 float,
#        预计新增门店数 int,
#        线下渠道预估轻饮酒总销量（瓶） int,
#        线下渠道预估蓝气罐总销量（箱） int,
#        预测销售总金额-二月 float,
#        预计新增门店数-二月 int,
#        线下渠道预估轻饮酒总销量（瓶）-二月 int,
#        线下渠道预估蓝气罐总销量（箱）-二月 int,
#        预测销售总金额-三月 float,
#        预计新增门店数-三月 int,
#        线下渠道预估轻饮酒总销量（瓶）-三月 int,
#        线下渠道预估蓝气罐总销量（箱）-三月 int,
#        销售预测 varchar(20),
#        大区-第一月线下 varchar(20),
#        省份-第一月线下 varchar(20),
#        区域-第一月线下 varchar(255),
#        大区-第二月线下 varchar(20),
#        省份-第二月线下 varchar(20),
#        区域-第二月线下 varchar(255),
#        大区-第三月线下 varchar(20),
#        省份-第三月线下 varchar(20),
#        区域-第三月线下 varchar(255),
#        电商平台 varchar(20),
#        备注 varchar(200)
#        预测销售总金额（三个月） float,
#     )


class ThirdMonthPredict:
    """
    三月预测表

    Attributes:
        predict_id: 预算制定流水号
        predict_man: 预算填写人
        predict_start_time: 预算期间
        predict_end_time: 预算截止期
        predict_part: 预算部门
        total_money_one:预测销售总金额
        increase_shops_one:预计新增门店数
        bottle_sale_one:线下渠道预估轻饮酒总销量（瓶）
        box_sale_one:线下渠道预估蓝气罐总销量（箱）
        total_money_two:预测销售总金额-二月
        increase_shops_two:预计新增门店数-二月
        bottle_sale_two:线下渠道预估轻饮酒总销量（瓶）-二月
        box_sale_two:线下渠道预估蓝气罐总销量（箱）-二月
        total_money_three:预测销售总金额-三月
        increase_shops_three:预计新增门店数-三月
        bottle_sale_three:线下渠道预估轻饮酒总销量（瓶）-三月
        box_sale_three:线下渠道预估蓝气罐总销量（箱）-三月
        predict_sale:销售预测
        area_one:大区-第一月线下
        province_one:省份-第一月线下
        region_one:区域-第一月线下
        area_two:大区-第二月线下
        province_two:省份-第二月线下
        region_two:区域-第二月线下
        area_three:大区-第三月线下
        province_three:省份-第三月线下
        region_three:区域-第三月线下
        platform:电商平台
        record:备注
        total_money_all:预测销售总金额（三个月）
        data_id: 这条记录在数据库里的id，通常不用, 默认-1
    """

    def __init__(self, predict_id: str, predict_man: str, predict_start_time: str, predict_end_time: str,
                 predict_part: str, total_money_one: float, increase_shops_one: int, bottle_sale_one: int,
                 box_sale_one: int, total_money_two: float, increase_shops_two: int, bottle_sale_two: int,
                 box_sale_two: int, total_money_three: float, increase_shops_three: int, bottle_sale_three: int,
                 box_sale_three: int, predict_sale: float, area_one: str, province_one: str, region_one: str,
                 area_two: str, province_two: str, region_two: str, area_three: str, province_three: str,
                 region_three: str, platform: str, record: str, total_money_all: float, data_id: int = -1):
        """

        :param predict_id: 预算制定流水号
        :param predict_man: 预算填写人
        :param predict_start_time: 预算期间
        :param predict_end_time: 预算截止期
        :param predict_part: 预算部门
        :param total_money_one: 预测销售总金额
        :param increase_shops_one: 预计新增门店数
        :param bottle_sale_one: 线下渠道预估轻饮酒总销量
        :param box_sale_one: 线下渠道预估蓝气罐总销量
        :param total_money_two: 预测销售总金额-二月
        :param increase_shops_two: 预计新增门店数-二月
        :param bottle_sale_two: 线下渠道预估轻饮酒总销量（瓶）-二月
        :param box_sale_two: 线下渠道预估蓝气罐总销量（箱）-二月
        :param total_money_three: 预测销售总金额-三月
        :param increase_shops_three: 预计新增门店数-三月
        :param bottle_sale_three: 线下渠道预估轻饮酒总销量（瓶）-三月
        :param box_sale_three: 线下渠道预估蓝气罐总销量（箱）-三月
        :param predict_sale: 销售预测
        :param area_one: 大区-第一月线下
        :param province_one: 省份-第一月线下
        :param region_one: 区域-第一月线下
        :param area_two: 大区-第二月线下
        :param province_two: 省份-第二月线下
        :param region_two: 区域-第二月线下
        :param area_three: 大区-第三月线下
        :param province_three: 省份-第三月线下
        :param region_three: 区域-第三月线下
        :param platform: 电商平台
        :param record: 备注
        :param total_money_all: 预测销售总金额（三个月）
        :param data_id: 这条记录在数据库里的id，通常不用, 默认-1
        """
        self.predict_id = predict_id
        self.predict_man = predict_man
        self.predict_start_time = predict_start_time
        self.predict_end_time = predict_end_time
        self.predict_part = predict_part
        self.total_money_one = total_money_one
        self.increase_shops_one = increase_shops_one
        self.bottle_sale_one = bottle_sale_one
        self.box_sale_one = box_sale_one
        self.total_money_two = total_money_two
        self.increase_shops_two = increase_shops_two
        self.bottle_sale_two = bottle_sale_two
        self.box_sale_two = box_sale_two
        self.total_money_three = total_money_three
        self.increase_shops_three = increase_shops_three
        self.bottle_sale_three = bottle_sale_three
        self.box_sale_three = box_sale_three
        self.predict_sale = predict_sale
        self.area_one = area_one
        self.province_one = province_one
        self.region_one = region_one
        self.area_two = area_two
        self.province_two = province_two
        self.region_two = region_two
        self.area_three = area_three
        self.province_three = province_three
        self.region_three = region_three
        self.platform = platform
        self.record = record
        self.total_money_all = total_money_all
        self.data_id = data_id

    def generate_tuple(self) -> Tuple:
        """
            返回一个用于插入新记录的有序元组。

        """
        return (self.predict_id, self.predict_man, self.predict_start_time, self.predict_end_time, self.predict_part,
                self.total_money_one,
                self.increase_shops_one, self.bottle_sale_one, self.box_sale_one, self.total_money_two,
                self.increase_shops_two, self.bottle_sale_two,
                self.box_sale_two, self.total_money_three, self.increase_shops_three, self.bottle_sale_three,
                self.box_sale_three, self.predict_sale,
                self.area_one, self.province_one, self.region_one, self.area_two, self.province_two, self.region_two,
                self.area_three, self.province_three,
                self.region_three, self.platform, self.record, self.total_money_all)


