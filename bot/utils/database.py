from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

from models import Base, User, Guild, Message, Warn

DATABASE_URI = 'sqlite:///mydatabase.db'

engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def add_user(username, email):
    with session_scope() as session:
        user = User(username=username, email=email)
        session.add(user)


def get_users():
    with session_scope() as session:
        users = session.query(User).all()
        return users


def delete_user(user_id):
    with session_scope() as session:
        user = session.query(User).filter_by(id=user_id).first()
        if user:
            session.delete(user)
            return True
        else:
            return False


def add_guild(name, owner_id):
    with session_scope() as session:
        guild = Guild(name=name, owner_id=owner_id)
        session.add(guild)


def get_guilds():
    with session_scope() as session:
        guilds = session.query(Guild).all()
        return guilds


def delete_guild(guild_id):
    with session_scope() as session:
        guild = session.query(Guild).filter_by(id=guild_id).first()
        if guild:
            session.delete(guild)
            return True
        else:
            return False


def add_message(content, author_id):
    with session_scope() as session:
        message = Message(content=content, author_id=author_id)
        session.add(message)


def get_messages():
    with session_scope() as session:
        messages = session.query(Message).all()
        return messages


def delete_message(message_id):
    with session_scope() as session:
        message = session.query(Message).filter_by(id=message_id).first()
        if message:
            session.delete(message)
            return True
        else:
            return False


def add_warn(user_id, guild_id, reason):
    with session_scope() as session:
        warn = Warn(user_id=user_id, guild_id=guild_id, reason=reason)
        session.add(warn)


def get_warns():
    with session_scope() as session:
        warns = session.query(Warn).all()
        return warns


def delete_warn(warn_id):
    with session_scope() as session:
        warn = session.query(Warn).filter_by(id=warn_id).first()
        if warn:
            session.delete(warn)
            return True
        else:
            return False
