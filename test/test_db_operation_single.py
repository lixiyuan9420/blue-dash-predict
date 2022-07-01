from db.operation.single_month import OneMonthPredict
from db.operation.single_month_sql import insert_single_month
from db.operation.third_month import ThirdMonthPredict
from db.operation.third_month_sql import insert_third_month
from db.standard import standard_update

# 常量
mock_data = {
    # 单月销量预测
    # 包含单月销量预测。
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
    #         备注 varchar(200),
    #         填写日期 int,
    #     )
    "单月销量预测": [
        ("test_data_0001", "李熙元", "IT部门", 1000.00, 10, 50, 50, "线下", "华东",
         "上海", "黄埔区", None, "test001", 202206)
    ],
    # 三月销量预测
    # 包含了三个月的销量预测
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
    #        填写日期 int
    #     )
    "三月销量预测": [
        ("test_data_0001", "李熙元", "7月", "9月", "IT技术部", 1000.00, 10, 50, 50, 1000.00, 10, 50, 50, 1000.00, 10, 50, 50,
         "线下", "华东", "上海",
         "黄埔", "华东", "上海", "黄埔", "华东", "上海", "黄埔", None, "test0001", 3000.00, 202206)
    ]
}


def __initial_db():
    """
    预先插入测试数据。

    :return: None
    """
    for single_month in mock_data["单月销量预测"]:
        try:
            insert_single_month(OneMonthPredict(*single_month))
        except Exception as e:
            print(e)

    for third_month in mock_data["三月销量预测"]:
        try:
            insert_third_month(ThirdMonthPredict(*third_month))
        except Exception as e:
            print(e)


def __clean_db():
    """
    删除测试数据。

    :return: None
    """
    for single_month in mock_data["单月销量预测"]:
        try:
            sql = "delete from 单月销量预测 where 预算制定流水号 = '%s'" % single_month[0]
            standard_update(sql, ())
        except Exception as e:
            print(e)

    for third_month in mock_data["三月销量预测"]:
        try:
            sql = "delete from 三月销量预测 where 预算制定流水号 = '%s'" % third_month[0]
            standard_update(sql, ())
        except Exception as e:
            print(e)


def test_db_operation_store():
    """
    本文件中用于测试的主函数。

    :return: None
    """
    __initial_db()

    __clean_db()


test_db_operation_store()
