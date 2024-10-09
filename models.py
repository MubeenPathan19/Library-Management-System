from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100))
    role = Column(String(20), nullable=False)  # 'LIBRARIAN' or 'MEMBER'

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))  # Specify length here
    author = Column(String(255))  # Specify length here
    status = Column(String(20), default="AVAILABLE")  # 'AVAILABLE' or 'BORROWED'

class Member(Base):
    __tablename__ = "members"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")
    status = Column(String(20), default="ACTIVE")  # 'ACTIVE' or 'DELETED'

class BorrowedBook(Base):
    __tablename__ = "borrowed_books"
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    member_id = Column(Integer, ForeignKey('members.id'))
    borrow_date = Column(DateTime)
    return_date = Column(DateTime, nullable=True)
    book = relationship("Book")
    member = relationship("Member")
