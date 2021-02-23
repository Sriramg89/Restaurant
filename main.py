from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.expression import null
from Models import models 
import DB_Models.db_models
from fastapi import FastAPI, Depends, Request
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session, session
# from Models.dmodel import get_db
from DB_Models.db_models import User,Restaurant,Menu_Category,Menu_Item
from Models.models import UserDetails, RestDetails, ItemDetails,CategDetails,UserEdit,RestEdit,ItemEdit,CategEdit
from DB_Models.db_models import SessionLocal, engine
from passlib.context import CryptContext                                                          
# from passlib.hash import bcrypt
# import bcrypt
rest = FastAPI()

pwd_context = CryptContext(schemes=["sha256_crypt", "md5_crypt", "des_crypt"], deprecated="auto")

def get_db():                                                           
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()        

DB_Models.db_models.Base.metadata.create_all(bind=engine)


# Endpoints for User Details

@rest.get("/user/all")                                                              
def user_details(db: Session = Depends(get_db)):
        data=db.query(User).all()
        return {"data":data}

@rest.get("/user/{entry}")                                                
def user_by_entry(entry: str, db: Session = Depends(get_db)):
    
    if(entry.isnumeric()==1):
       
        data = db.query(User).filter(User.id == entry).all()
        return {"data":data}

    else:

        data = db.query(User).filter(User.email == entry).all()
        return {"data":data}     

@rest.post("/user/")                                                    
def create_user(detail_request: UserDetails, db: Session = Depends(get_db)):

    post = User()                                                                                                      
    post.name=detail_request.name
    post.email=detail_request.email
    post.password=pwd_context.hash(detail_request.password)
   
        
    db.add(post)
    db.commit()
    return {
        "code": "success",
        "message": "User details added to the database"
    }    

@rest.delete("/user/{id}")                                             
def del_user_by_id(id:int, db: Session = Depends(get_db)):
   
    db.query(User).filter(User.id == id).delete()
    db.commit()
    # data=db.query(Blog).all()
    return {
        "code": "success",
        "message": "User details deleted from the database"} 

@rest.put("/user/{id}")
def update_user(id: int, item: UserEdit, db: Session = Depends(get_db)):
    
    update_item_encoded = {i: jsonable_encoder(item)[i] for i in jsonable_encoder(item) if jsonable_encoder(item)[i]!=None}
    db.query(User).filter(User.id==id).update(update_item_encoded)
    
    db.commit()
    data= db.query(User).filter(User.id==id).first()
    return data

# Endpoints for Restaurant Details

@rest.get("/rest/all")                                                              
def rest_details(db: Session = Depends(get_db)):
        data=db.query(Restaurant).all()
        return {"data":data}

@rest.get("/rest/{id}")                                                
def rest_by_id(id: int, db: Session = Depends(get_db)):
       
        data = db.query(Restaurant).filter(Restaurant.id == id).all()
        return {"data":data}

@rest.get("/rest/user/{id}")                                                
def rest_by_id(id: int, db: Session = Depends(get_db)):
       
        data = db.query(Restaurant).filter(Restaurant.userid == id).all()
        return {"data":data}

@rest.post("/rest/")                                                    
def create_rest(detail_request: RestDetails, db: Session = Depends(get_db)):

    post = Restaurant()                                                                                                      
    post.name=detail_request.name
    post.address=detail_request.address
    post.open_time=detail_request.open_time
    post.close_time=detail_request.close_time
    post.userid=detail_request.userid
        
    db.add(post)
    db.commit()
    return {
        "code": "success",
        "message": "Restaurant details added to the database"
    }    

@rest.delete("/rest/{id}")                                             
def del_rest_by_id(id:int, db: Session = Depends(get_db)):
   
    db.query(Restaurant).filter(Restaurant.id == id).delete()
    db.commit()
    # data=db.query(Blog).all()
    return {
        "code": "success",
        "message": "Restaurant details deleted from the database"} 

@rest.put("/rest/{id}")
def update_rest(id: int, item: RestEdit, db: Session = Depends(get_db)):
    
    update_item_encoded = {i: jsonable_encoder(item)[i] for i in jsonable_encoder(item) if jsonable_encoder(item)[i]!=None}
    db.query(Restaurant).filter(Restaurant.id==id).update(update_item_encoded)
    
    db.commit()
    data= db.query(Restaurant).filter(Restaurant.id==id).first()
    return data

# Endpoints for Menu Category Details

@rest.get("/categ/all")                                                              
def category_details(db: Session = Depends(get_db)):
        data=db.query(Menu_Category).all()
        return {"data":data}

@rest.get("/categ/{id}")                                                
def categ_by_id(id: int, db: Session = Depends(get_db)):
    
    data = db.query(Menu_Category).filter(Menu_Category.id == id).all()
    return {"data":data}
    

@rest.post("/categ/")                                                    
def create_user(detail_request: CategDetails, db: Session = Depends(get_db)):

    post = Menu_Category()                                                                                                      
    post.name=detail_request.name
    post.description=detail_request.description
    post.restid=detail_request.restid
    
        
    db.add(post)
    db.commit()
    return {
        "code": "success",
        "message": "Menu details added to the database"
    }    

@rest.delete("/categ/{id}")                                             
def del_categ_by_id(id:int, db: Session = Depends(get_db)):
   
    db.query(Menu_Category).filter(Menu_Category.id == id).delete()
    db.commit()
    # data=db.query(Blog).all()
    return {
        "code": "success",
        "message": "Menu details deleted from the database"} 

@rest.put("/categ/{id}")
def update_categ(id: int, item: CategEdit, db: Session = Depends(get_db)):
    
    update_item_encoded = {i: jsonable_encoder(item)[i] for i in jsonable_encoder(item) if jsonable_encoder(item)[i]!=None}
    db.query(Menu_Category).filter(Menu_Category.id==id).update(update_item_encoded)
    
    db.commit()
    data= db.query(Menu_Category).filter(Menu_Category.id==id).first()
    return data


# Endpoints for Menu Item Details

@rest.get("/item/all")                                                              
def item_details(db: Session = Depends(get_db)):
        data=db.query(Menu_Item).all()
        return {"data":data}

@rest.get("/item/{id}")                                                
def item_by_name(id: int, db: Session = Depends(get_db)):

        data = db.query(Menu_Item).filter(Menu_Item.id == id).all()
        return {"data":data}

@rest.get("/item/categ/{id}")                                                
def item_by_id(id: int, db: Session = Depends(get_db)):

        data = db.query(Menu_Item).filter(Menu_Item.categid == id).all()
        return {"data":data}


@rest.post("/item/")                                                    
def create_item(detail_request: ItemDetails, db: Session = Depends(get_db)):

    post = Menu_Item()                                                                                                      
    post.name=detail_request.name
    post.description=detail_request.description
    post.categid=detail_request.categid
    post.cost=detail_request.cost
    
        
    db.add(post)
    db.commit()
    return {
        "code": "success",
        "message": "Item details added to the database"
    }    

@rest.delete("/item/{id}")                                             
def del_item_by_id(id:int, db: Session = Depends(get_db)):
   
    db.query(Menu_Item).filter(Menu_Item.id == id).delete()
    db.commit()
    # data=db.query(Blog).all()
    return {
        "code": "success",
        "message": "Item details deleted from the database"} 

@rest.put("/item/{id}")
def update_item(id: int, item: ItemEdit, db: Session = Depends(get_db)):
    
    update_item_encoded = {i: jsonable_encoder(item)[i] for i in jsonable_encoder(item) if jsonable_encoder(item)[i]!=None}
    db.query(Menu_Item).filter(Menu_Item.id==id).update(update_item_encoded)
    
    db.commit()
    data= db.query(Menu_Item).filter(Menu_Item.id==id).first()
    return data




