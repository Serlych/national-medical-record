#!/usr/bin/env python3
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from prescription_model import Prescription, PrescriptionUpdate

router = APIRouter()

@router.post("/", response_description="Post the info of a new medication", status_code=status.HTTP_201_CREATED, response_model=Prescription)
def create_prescription(request: Request, prescription: Prescription = Body(...)):
    #prescription = jsonable_encoder(prescription)
    print (prescription)
    # new_prescription = request.app.database["prescriptions"].insert_one(prescription)
    # created_prescription = request.app.database["prescriptions"].find_one(
    #     {"_id": new_prescription.inserted_id}
    # )

    # return created_prescription


# @router.get("/", response_description="Get all books", response_model=List[Book])
# def list_books(request: Request, rating: float = 0, title: str = "", limit: int = 5, skip: int = 0, pages: int = 0):
#     books = list(request.app.database["books"].find({"average_rating": {"$gte": rating}, "$text": {"$search": title}, "num_pages":{"$gte": pages}}).limit(limit).skip(skip))
#     return books


# @router.get("/{id}", response_description="Get a single book by id", response_model=Book)
# def find_book(id: str, request: Request):
#     if (book := request.app.database["books"].find_one({"_id": id})) is not None: #book = request.app.database["books"].find_one({"_id": id}) 
#         return book                                                               #if book: return book

#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {id} not found")

# @router.put("/{id}", response_description="Update a book", response_model=BookUpdate)
# def update_book(id: str, request: Request, book: BookUpdate = Body(...)):
#     book = jsonable_encoder(book)

#     for key, value in book.items(): 
#         if value is None: 
#             pass
#         else:
#             book = {key:value}    
      
#     if (updated_book := request.app.database["books"].find_one_and_update({"_id": id}, 
#                         {'$set' : book})) is not None:
#         return updated_book
    
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {id} not found")                 

# @router.delete("/{id}", response_description="Delete a book")
# def delete_book(id: str, request:Request):
       
#     if (delete_book := request.app.database["books"].delete_one({"_id": id})) is not None:
#         return 
    
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {id} not found") 