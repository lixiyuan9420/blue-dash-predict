import re

from util.format import extract_ym_from_int


def positive_time(predict_time, write_time) -> int:
    year, month = extract_ym_from_int(write_time)
    predict_month = re.findall(r'd+', predict_time)
    return predict_month[0] - month

#
# class Compute:
#     """
#     用于计算销售的差额和达成率
#     Attributes:
#         region: 销售大区
#
#     """
