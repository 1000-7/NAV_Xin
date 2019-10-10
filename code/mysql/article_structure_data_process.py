import pymysql
from others.logging import logger, init_logger

db = pymysql.connect("192.168.1.104", "root", "irlab2017", "graduate", charset='utf8')
init_logger("../../logs/mysql_article_structure1.log")

cursor = db.cursor()

sql = "SELECT * FROM semanticScholar_type2_1"
logger.info(sql)

# 执行SQL语句
cursor.execute(sql)

# 获取所有记录列表
results = cursor.fetchall()
logger.info("fetch finished")
for row in results:
    data_id = row[0]
    paper_section = (row[2].replace("- ", ""))
    if paper_section.find("is organized as follows") >= 0:
        logger.info(paper_section)

