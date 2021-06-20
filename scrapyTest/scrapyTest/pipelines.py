# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql

class MySQLPipeline(object):

    # 打开数据库
    def open_spider(self, spider):
        db = spider.settings.get('MYSQL_DB_NAME', 'win')
        host = spider.settings.get('MYSQL_HOST', 'localhost')
        port = spider.settings.get('MYSQL_PORT', 3306)
        user = spider.settings.get('MYSQL_USER', 'root')
        passwd = spider.settings.get('MYSQL_PASSWORD', '1')

        self.db_conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8')
        self.db_cur = self.db_conn.cursor()
        sql1 = "delete from ball"
        self.db_cur.execute(sql1)
        print("======open_spider=====")

    # 关闭数据库
    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    # 对数据进行处理
    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    #插入数据
    def insert_db(self, item):
        values = (
            item['periods'],
            item['redBall1'],
            item['redBall2'],
            item['redBall3'],
            item['redBall4'],
            item['redBall5'],
            item['redBall6'],
            item['blueBall'],

        )
        try:
            sql2 = "insert into ball (periods,red1,red2,red3,red4,red5,red6,blue) values (%s,%s,%s,%s,%s,%s,%s,%s)"
            self.db_cur.execute(sql2, values)
            print(self.db_cur._last_executed)
            self.db_conn.commit()
            print("Insert finished")
        except:
            print("Insert to DB failed")
            self.db_conn.commit()
            self.db_conn.close()
