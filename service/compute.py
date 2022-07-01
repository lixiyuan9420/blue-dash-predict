import re
from typing import Tuple

from util.format import extract_ym_from_int


def positive_time(predict_time, write_time) -> int:
    year, month = extract_ym_from_int(write_time)
    predict_month = re.findall(r'd+', predict_time)
    return predict_month[0] - month

# TODO

# def choose_way(predict_time, write_time):
#     positive = positive_time(predict_time,write_time)
#     if positive == 3:
#         # 插入
#     elif positive == 2:
#         # 更新
#     elif positive == 1:
#         #更新
#     else:
#


