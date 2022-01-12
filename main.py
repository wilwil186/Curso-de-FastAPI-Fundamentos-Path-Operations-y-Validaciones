#Python
from typing import Optional
from fastapi.param_functions import Query 
#Pydantic
from pydantic import BaseModel #capaz de crear modelos
#FastAPI
from fastapi import FastAPI # impotar FastAPI
from fastapi import Body # es una clase de fast que permite decir que un paramtro es de tipo body
from fastapi import Query
app = FastAPI() #instancia

#Models
class Person(BaseModel):
    first_name: str
    las_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None

@app.get("/") #path operations
def home():
    return {"Hello": "World"}

# Request and Response Body

@app.post("/person/new")
def create_person(person: Person = Body(...)): #un request body tambien es parametro 
    return person

# Validaciones: Query parameters

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(None, min_length=1, max_length=50),
    age: str = Query(...)
): 
    return {name: age}