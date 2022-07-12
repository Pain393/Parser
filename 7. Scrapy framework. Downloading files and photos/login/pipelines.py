# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3

from itemadapter import ItemAdapter

class LoginPipeline:
    def open_spider(self, spider):
        self.connection = sqlite3.connect('login.db')
        self.cursor = self.connection.cursor()

        create_table_query = '''
            CREATE TABLE all_team(
                Division TEXT,
                RK TEXT,
                Team TEXT,
                W TEXT,
                L TEXT,
                OL TEXT,
                PTS TEXT
            )
        '''
        try:
            self.cursor.execute(create_table_query)
            self.connection.commit()
        except sqlite3.OperationalError:
            pass

    def process_item(self, item, spider):


        insert_query = '''
            INSERT INTO all_team(Division, RK, Team, W, L, OL, PTS)
                VALUES (?,?,?,?,?,?,?)
        '''
        self.cursor.execute(insert_query, (item.get('Division'), item.get('RK'), item.get('Team'),
                                           item.get('W'), item.get('L'), item.get('OL'), item.get('PTS')))
        self.connection.commit()

    def close_spider(self, spider):
        self.connection.close()
