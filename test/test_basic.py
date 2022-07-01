from db.standard import standard_query, standard_update
from logger.logger import errLogger
import traceback


def test_standard_query():
    standard_query("select * from table_not_exist")


def test_standard_update():
    standard_update("update table_not_exist set attr1 = 'hello world' where attr2 = '!'")


def test_all():
    # 这两个一定会报错
    try:
        test_standard_query()
        test_standard_update()
    except Exception as e:
        errLogger.log(e, enable_traceback=True, line_below=True)


test_all()
