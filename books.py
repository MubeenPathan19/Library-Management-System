from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import BookCreate
from app.models import Book
from app.database import get_db

router = APIRouter()

@router.post("/add-book")
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = Book(title=book.title, author=book.author)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@router.get("/books")
def get_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books
