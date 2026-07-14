books=[
  {
    "id": 1,
    "title": "The Great Gatsby",  
    "author": "F. Scott Fitzgerald",
    "published_year": 1925
  },
  {
    "id": 2,
    "title": "To Kill a Mockingbird", 
    "author": "Harper Lee",
    "published_year": 1960

  },{
    
    "id": 3,
    "title": "1984",  
    "author": "George Orwell",
    "published_year": 1948

  }
]
import email

from fastapi import FastAPI,status
from pydantic import BaseModel
from fastapi.exceptions import HTTPException
app=FastAPI()
@app.get("/books")
def get_books():
    return books

class BOOK(BaseModel):
    id: int
    title: str
    author: str
    published_year: int

@app.post("/book")
def add_book(book: BOOK):
   new_book=book.model_dump()
   books.append(new_book)

class BOOK2(BaseModel):
    title :str
    author:str
    published_year:int

@app.put("/fetch/{book_id}")
def fetch_book(book_id:int,book:BOOK2):
    for b in books:
        if(b["id"]==book_id):
            b["title"]=book.title
            b["author"]=book.author
            b["published_year"]=book.published_year

@app.delete("/del/{book_id}")
def del_book(book_id:int):
    for b in books:
        if(b["id"]==book_id):
            books.remove(b)
            return
     
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="book not found")