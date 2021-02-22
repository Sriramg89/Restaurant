from typing import Optional
from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.sqltypes import NullType
from fastapi import FastAPI, Depends, Request                                             
from pydantic import BaseModel                                      
from sqlalchemy.orm import Session, session
import datetime
import sys


class UserDetails(BaseModel):                                         
    
    
    name : str
    email : str
    password : str
    

class RestDetails(BaseModel):                                         
    
    
    name : str
    address : str
    open_time : str
    close_time : str
    userid: int

class ItemDetails(BaseModel):                                         
    
    
    categid : int
    name : str 
    description : str
    cost : int

class CategDetails(BaseModel):                                         
    
    name : str 
    description : str   
    restid : int 

class UserEdit(UserDetails):
    
    name : Optional[str]
    email : Optional[str]
    password : Optional[str]
   

class RestEdit(RestDetails):
    
    name : Optional[str]
    address : Optional[str]
    open_time : Optional[str]
    close_time : Optional[str]
    userid : Optional[int]

class ItemEdit(ItemDetails):
    
    categid : Optional[int]
    name : Optional[str] 
    description : Optional[str]
    cost : Optional[int]

class CategEdit(CategDetails):
    
    name : Optional[str] 
    description : Optional[str]   
    restid : Optional[int] 
      
