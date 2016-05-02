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
        """
        Returns the entries in the database, ordered so that the most recent entry is first.

        :param: none
        :return: the entries in the databse, ordered so that the most recent entry is first
        """
        return select([Entry.id, Entry.title, Entry.body, Entry.created, Entry.edited]).select_from(
            Entry).order_by(Entry.edited.desc())

    @classmethod
    def by_id(cls, given_id):
        """
        Returns a single entry in the database with the given id.

        :param: given_id - the id to search in the database
        :return: the single entry with the corresponding given id
        """
        return select([Entry.id, Entry.title, Entry.body, Entry.created, Entry.edited]).select_from(
            Entry).where(Entry.id == given_id)
