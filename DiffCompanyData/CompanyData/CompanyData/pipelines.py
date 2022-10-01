# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# import sqlite3
import pymongo
from itemadapter import ItemAdapter


class CompanydataPipeline:

    def __init__(self):
        # self.create_connection()
        # self.create_table()
        self.conn = pymongo.MongoClient('localhost',27017)
        db = self.conn('CompanyData')
        self.collection = db['Company_tb']
    
    # def create_connection(self):
    #     # self.conn = mysql.connector.connect(
    #     #     host = 'localhost',
    #     #     user = 'root',
    #     #     passwd = 'root@mysql',
    #     #     database = 'imdb'
    #     # )
    #     self.conn = sqlite3.connect('CompanyData.db')
    #     self.curr = self.conn.cursor()
    
    # def create_table(self):
    #     self.curr.execute("""DROP TABLE IF EXISTS Company_Data""")
    #     self.curr.execute("""create table Company_Data(
    #                         Company_name text,
    #                         Founders text,
    #                         Type text
    #                         )""")

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item

    # def store_db(self, item):
        
    #     self.curr.execute("""insert into Company_Data values(?,?,?)""",(
    #         item['Company_name'][0],
    #         item['Founders'][0],
    #         item['Type_Of_Company'][0]
    #     ))
    #     self.conn.commit()
