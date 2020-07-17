import datetime
from grapevine.models.meta import Base
from sqlalchemy import (
    Column,
    Integer,
    Unicode,  # <- will provide Unicode field
    UnicodeText,  # <- will provide Unicode text field
    DateTime,  # <- time abstraction field
)

from passlib.apps import custom_app_context as context

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), unique=True, nullable=False)
    password = Column(Unicode(255), nullable=False)
    last_logged = Column(DateTime, default=datetime.datetime.utcnow)

    def verify_password(self, password):
        # is it cleartext?
        if password == self.password:
            self.set_password(password)

        return context.verify(password, self.password)

    def set_password(self, password):
        password_hash = context.encrypt(password)
        self.password = password_hash
