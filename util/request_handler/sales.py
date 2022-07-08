from typing import Tuple, Optional

from db.operation.sales import Sales
from util.request_handler.common import convert_to_int, verify_auth_token


def extract_sales(data_json) -> Sales:
    """
        从JSON结构体中抽取出一个实际销量。
        JSON结构体应该格式如下：
        e.g., {
                "销售订单销量":
                {
	                "销售单号":"xxx",
	                "蓝气罐销量":100,
                    "轻饮酒销量":100,
                    "填写日期":202206,
                    "归属大区":"xxx"
                }
            }
        :param data_json: JSON
        :return:OneMonthPredict
        """
    data = data_json["销售订单销量"]
    sales_id = data["销售单号"]
    box_sale = convert_to_int(data["蓝气罐销量"])
    bottle_sale = convert_to_int(data["轻饮酒销量"])
    date = convert_to_int(data["填写日期"])
    area = data["归属大区"]
    return Sales(sales_id, box_sale, bottle_sale, date, area)


def __extract_reality_query(data_json) -> Tuple[Optional[str], Optional[str]]:
    """
    处理json数据
    :param data_json:
    :return:
    """
    data = data_json["查询销量数据"]
    region = str(data["大区"])
    year_month = str(data["指定年月"])
    return region, year_month


def verified_reality_query(data_json) -> Tuple[Optional[str], Optional[str]]:
    """
    抽取出一个用于查询或计算销售人员提成的元组。 抽取出的结果为：销售人员编号，销售人员姓名，年，月。
    JSON结构体例子：

    e.g., {

    "查询销量数据“: {

        "大区": "xxx",
        "指定年月": "xxx",建议不为空

    },
    "token": "abcdefg123"
    }

    :param data_json: JSON
    :return: Tuple[Optional[str], Optional[str], int, int]
    """
    if verify_auth_token(data_json):
        return __extract_reality_query(data_json)
    raise ValueError("验证身份信息失败！")
