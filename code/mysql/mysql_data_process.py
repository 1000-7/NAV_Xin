import pymysql
from others.logging import logger

# db = pymysql.connect("localhost", "root", "irlab2017", "graduate", charset='utf8')
db = pymysql.connect("localhost", "root", "wx1996", "graduate", charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

for iter in range(0, 10):
    logger.info("now batch is:" + str(iter))
    sql = "SELECT * FROM semanticScholar_filter limit " + str(iter * 200000) + "," + str(200000) + ";"
    logger.info(sql)

    # 执行SQL语句
    cursor.execute(sql)

    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        type1 = row[6]