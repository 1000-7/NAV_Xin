import pymysql
from others.logging import logger, init_logger

# db = pymysql.connect("localhost", "root", "irlab2017", "graduate", charset='utf8')
db = pymysql.connect("localhost", "root", "wx1996", "graduate", charset='utf8')
init_logger("../../logs/test.log")
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
        data_id = row[0]
        paper_section = row[2].replace("- ", "")
        summary_sentence = row[3].replace("- ", "")
        with open('/Users/unclewang/PycharmProjects/NAV_Xin/data/' + str(data_id) + '.story', 'w') as fw:
            fw.write(paper_section + "\n")
            fw.write("@highlight")
            fw.write(summary_sentence)
        break
