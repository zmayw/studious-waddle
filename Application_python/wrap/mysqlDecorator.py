#coding=utf-8

from functools import wraps
import sys
class Configuration:

    def __init__(self, env):
        if env == "Prod" :
            self.host = "coolshell.cn"
            self.port = 3306
            self.db = "coolshell"
            self.user = "coolshell"
            self.passwd = "fuckgfw"

        elif env == "Test":
            self.host = 'localhost'
            self.port = 3300
            self.user = "coolshell"
            self.db = "coolshell"
            self.passwd = "fuckfw"

def mysql(sql):
    _conf = Configuration(env="Prod")

    def on_sql_error(err):
        print err
        sys.exit(-1)

    def handle_sql_result(rs):
        if rs.rows > 0 :
            fieldnames = [f[0] for f in rs.fields]
            return [dict(zip(fieldnames, r)) for r in rs.rows]
        else:
            return []

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            mysqlconn = umysql.Connection()
            mysqlconn.settimeout(5)
            mysqlconn.connect(_conf.host,_conf.port,_conf.user,_conf.passwd,_conf.db,True, "utf8")

            try:
                rs = mysqlconn.query(sql,{})
            except umysql.Error as e:
                on_sql_error(e)

            data = handle_sql_result(rs)
            kwargs["data"] = data
            result = fn(*args, **kwargs)
            mysqlconn.close()
            return result
        return wrapper
    return decorator

#test
@mysql(sql="select * from coolshell")
def get_coolshell(data):
    pass #


