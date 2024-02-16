from eastvantage import app
import logging
from pydantic import BaseModel

logging.basicConfig()
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)



class Book(BaseModel):
    title: str
    author: str
    publication_year: int

class ReviewBook(BaseModel):
    text: str
    rating: int

@app.get("/")
def root():
    return "Running.......!!!!"


bookList = []

# 1. ADD NEW BOOK
@app.post("/books/")
def add_book(book: Book):
    bookList.append(book)
    return {"message": "Book added successfully"}

# 2. Submit a review for a book