from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    String,
    Unicode,
    DateTime,
    select,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

import datetime

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class Entry(Base):
    __tablename__ = 'entries'
    id = Column('id', Integer, primary_key=True)
    title = Column('title', String(255), nullable=False, unique=True)
    body = Column('body', Unicode)
    created = Column('created', DateTime, default=datetime.datetime.now)
    edited = Column('edited', DateTime, default=datetime.datetime.now)

    @classmethod
    def all(cls):
        return select([Entry.id, Entry.title, Entry.body, Entry.created, Entry.edited]).select_from(Entry).order_by(Entry.edited.desc())

    @classmethod
    def by_id(cls, given_id):
        return select([Entry.id, Entry.title, Entry.body, Entry.created, Entry.edited]).select_from(Entry).where(Entry.id == given_id)

