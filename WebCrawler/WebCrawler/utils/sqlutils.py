from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from WebCrawler.dbbase import Zhihu_User_Info as Table


class SQLUtils(object):
    def __init__(self):
        engine = create_engine('mysql+pymysql://root:root@localhost/zhihu?charset=utf8', echo=False)
        session_cls = sessionmaker(bind=engine)
        self.session = session_cls()

    def query_url_token(self, row):
        query = self.session.query(Table.id). \
            filter(Table.url_token == row.url_token)
        return query.first()

    def add_to_db(self,row):
        try:
            self.session.add(row)
            self.session.commit()
        except Exception,e:
            print 'error:',e
            self.session.rollback()
        finally:
            pass

    def item_to_row(self, item):
        return Table.transform(item)