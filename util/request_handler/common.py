from util.auth import auth_by_token


def convert_to_int(a):
    try:
        r = int(a)
    except:
        r = 0
    return r


def convert_to_float(a):
    try:
        r = float(a)
    except:
        r = 0.0
    return r


def convert_to_bool(a):
    if type(a) == bool:
        return a
    else:
        if a in [1, "True", "true"]:
            return True
        return False


def __extract_auth_token(data_json) -> str:
    """
    从JSON结构体中获取一个用于验证身份的token。
    JSON结构体应该格式如下：

    e.g., {"token": "abcdefg123"}

    :param data_json: JSON
    :return: str
    """
    return data_json["token"]


def verify_auth_token(data_json) -> bool:
    """
    从JSON结构体中获取一个用于验证身份的token，并检验有效性。
    JSON结构体应该格式如下：

    e.g., {"token": "abcdefg123"}

    :param data_json: JSON
    :return: bool
    """
    return auth_by_token(__extract_auth_token(data_json))
