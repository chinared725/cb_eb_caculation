import pymysql

def remove_per (str):
    str = str[:-1]
    return str

def data_process(data, columns):
    for col in columns:
        data[col+'1'] = data[col].apply(remove_per).convert_objects(convert_numeric=True) * 0.01
    return data.convert_objects(convert_numeric=True)

def get_name_part(str):
    str = str[-2:]
    return str

def get_bond_time(str):

    if str != '待上市':
        str = str[-8:]
    return str


def mysql_conn(db_name):  # 为了方便数据库连接的函数
    try:
        db = pymysql.connect('localhost', 'root', 'china12345', db_name, charset='utf8')
        print("connect mysql server success")
        return db
    except:
        db.rollback()
        print('could not connect to mysql server')




def execute_sql_no_return(sql, db):  # 进行无返回的数据库操作的函数，比如create table
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        print('execute sql success')
    except:
        db.rollback()
        print('execute sql fail')


def execute_sql_with_return(sql, db):  # 进行有返回的数据库操作的函数，比如select
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        print('execute sql success')
        return cursor.fetchall()
    except:
        db.rollback()
        print('execute sql fail')
