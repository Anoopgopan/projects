from fastapi import FastAPI,HTTPException,Query
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

class Book(BaseModel):
    title: str
    author: str
    publication_year: int

class Review(BaseModel):
    text: str
    rating: int
app = FastAPI()


@app.get("/")
def root():
    return {"message":"running...!!"}


bookList = []
reviewList = []

# 1. add a new book
@app.post("/books")
def add_book(book: Book):
    bookList.append(book)
    return {"message": "Book added successfully"}

# 2. Submit a review for a book
@app.post("/books/{book_id}/reviews/")
def submit_review(book_id: int, review: Review):
    
    if book_id < 0 or book_id >= len(bookList):
        raise HTTPException(status_code=404, detail="Book not found")
    
    reviewList.append({"book_id": book_id, **review.dict()})
    return {"message": "Review submitted successfully"}

# 3. Retrieve all books with an option to filter by author or publication year.
def get_books(author: Optional[str] = None, publication_year: Optional[int] = None):
    
    filtered_books = bookList
    
    if author:
        filtered_books = [b for b in filtered_books if b.author == author]
    
    if publication_year:
        filtered_books = [b for b in filtered_books if b.publication_year == publication_year]
    return filtered_books

# 4. Retrieve all reviews for a specific book.
@app.get("/books/{book_id}/reviews/", response_model=List[Review])
def get_reviews(book_id: int):
    
    if book_id < 0 or book_id >= len(bookList):
        raise HTTPException(status_code=404, detail="Book not found")
    
    book_reviews = [review for review in reviewList if review["book_id"] == book_id]
    
    if not book_reviews:
        raise HTTPException(status_code=404, detail="No reviews found for the specified book")

    return book_reviews

# 5. Error Handling: Implement proper error handling for invalid requests.
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {"error": exc.detail}

# 6. Internal server error 
@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return {"error": "Internal server error"}


# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.0", port=8000)





