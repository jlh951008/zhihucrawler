from sqlalchemy import Column, INT, VARCHAR, BINARY
from sqlalchemy.ext.declarative import declarative_base

_Base = declarative_base()


class Zhihu_User_Info(_Base):
    __tablename__ = 'zhihu_user_info'
    id = Column('id', INT, nullable=False, default=None,autoincrement=True, primary_key=True)
    url_token = Column('url_token', VARCHAR(32), nullable=False, default=None)
    name = Column('name', VARCHAR(64), nullable=True, default=None)
    uid = Column('uid', BINARY(64), nullable=False, default=None)
    follower_count = Column('follower_count', INT, nullable=True, default=None)
    answer_count = Column('answer_count', INT, nullable=True, default=None)

    @classmethod
    def transform(cls,item):
        return cls(#id=item.get('id'),
                   url_token=(item.get('url_token')),
                   name=item.get('name').encode('utf-8'),
                   uid=item.get('uid'),
                   follower_count=item.get('follower_count'),
                   answer_count=item.get('answer_count'),
                   )


