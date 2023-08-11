from database import Base
from sqlalchemy import Column, String, BigInteger, DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

# таблица пользователей
class User(Base):
    __tablename__ = "users"
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    profile_photo = Column(String)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    phone_number = Column(BigInteger, nullable=False)
    email = Column(String, nullable=False)
    city = Column(String)
    reg_date = Column(DateTime)
    password = Column(String, nullable=False)
# таблица карт
class Card(Base):
    __tablename__ = "cards"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("user.id"), nullable=False)
    card_number = Column(BigInteger, nullable=False, unique=True)
    exp_data = Column(Integer, nullable=False)
    card_balance = Column(Float, default=15000)
    card_name = Column(String, default="My card")
    reg_date = Column(DateTime)
    user_fk = relationship(User, lazy="subquery")
# таблица платежей
class Transaction(Base):
    __tablename__ = "user_transactions"
    card_from: int
    amount: float
    card_to: int
    transfer_time = None
# таблица категорий платежей
