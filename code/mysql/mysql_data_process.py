import pymysql
from others.logging import logger, init_logger

db = pymysql.connect("localhost", "root", "irlab2017", "graduate", charset='utf8')
# db = pymysql.connect("localhost", "root", "wx1996", "graduate", charset='utf8')
init_logger("../../logs/mysql.log")
# 使用cursor()方法获取操作游标
cursor = db.cursor()

for iter in range(0, 11):
    logger.info("now batch is:" + str(iter))
    sql = "SELECT * FROM semanticScholar_filter limit " + str(iter * 200000) + "," + str(200000) + ";"
    logger.info(sql)

    # 执行SQL语句
    cursor.execute(sql)

    # 获取所有记录列表
    results = cursor.fetchall()
    finishNum = 0
    for row in results:
        data_id = row[0]
        paper_section = row[2].replace("- ", "")
        summary_sentence = row[3].replace("- ", "").replace("\n", "")
        with open('/home/wangxin/PycharmProjects/nav_story/' + str(data_id) + '.story', 'w') as fw:
            fw.write(paper_section + "\n")
            fw.write("@highlight" + "\n")
            fw.write(summary_sentence)

        if finishNum % 10000 == 0:
            logger.info("has finished " + str(finishNum))
        finishNum += 1
