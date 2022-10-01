# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# import mysql.connector
# import sqlite3
import pymongo

from itemadapter import ItemAdapter


class AmitabhPipeline:
    def __init__(self):
        # self.create_connection()
        # self.create_table()
        # self.conn = pymongo.MongoClient('0.tcp.ngrok.io',17467,username='root',password='password')
        self.conn = pymongo.MongoClient('0.tcp.ngrok.io',18990)

        db = self.conn['CompanyData']
        self.collection = db['Company_tb']
    
    # def create_connection(self):
    #     # self.conn = mysql.connector.connect(
    #     #     host = 'localhost',
    #     #     user = 'root',
    #     #     passwd = 'root@mysql',
    #     #     database = 'imdb'
    #     # )
    #     self.conn = sqlite3.connect('movies.db')
    #     self.curr = self.conn.cursor()
    
    # def create_table(self):
    #     self.curr.execute("""DROP TABLE IF EXISTS Amitabh_Data""")
    #     self.curr.execute("""create table Amitabh_Data(
    #                         Movie_name text
    #                         )""")

    def process_item(self, item, spider):
        # self.store_db(item)
        self.collection.insert(dict(item))
        return item

    # def store_db(self, item):
    #     for i in range(0,len(item['movie_name'])):
    #         self.curr.execute("""insert into Amitabh_Data values(?)""",(
    #             [item['movie_name'][i]]
    #             # item['released_in_year']
    #         ))
    #     self.conn.commit()

