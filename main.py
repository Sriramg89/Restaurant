from sqlalchemy.sql.expression import null
import DB_Models
from Models import *
from DB_Models import *
from fastapi import FastAPI, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from DB_Models import Orders, User, Restaurant
from DB_Models.Menu.menu import *
from Models.Order.order import *
from Models.Menu.menu import *
from Models.User.user import *
from Models.Restaurant.restaurant import *
from DB_Models.database import SessionLocal, engine
from passlib.context import CryptContext

rest = FastAPI()

pwd_context = CryptContext(
    schemes=[
        "sha256_crypt",
        "md5_crypt",
        "des_crypt"],
    deprecated="auto")


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


DB_Models.database.Base.metadata.create_all(bind=engine)


# Endpoints for User Details

@rest.get("/user/all")
def user_details(db: Session = Depends(get_db)):
    data = db.query(User).all()
    return {"data": data}


@rest.get("/user/{entry}")
def user_by_entry(entry: str, db: Session = Depends(get_db)):

    if(entry.isnumeric() == 1):

        data = db.query(User).filter(User.id == entry).all()
        return {"data": data}

    else:

        data = db.query(User).filter(User.email == entry).all()
        return {"data": data}


@rest.post("/user/", response_model=UserDetails)
def create_user(detail_request: UserDetails, db: Session = Depends(get_db)):

    post = User()
    post.name = detail_request.name
    post.email = detail_request.email
    post.password = pwd_context.hash(detail_request.password)
    post.mobile = detail_request.mobile
    post.age = detail_request.age

    db.add(post)
    db.commit()
    return detail_request


@rest.delete("/user/{id}")
def del_user_by_id(id: int, db: Session = Depends(get_db)):

    db.query(User).filter(User.id == id).delete()
    db.commit()

    return {
        "code": "success",
        "message": "User details deleted from the database"}


@rest.put("/user/{id}")
def update_user(id: int, item: UserEdit, db: Session = Depends(get_db)):

    update_item_encoded = {i: jsonable_encoder(item)[i] for i in jsonable_encoder(
        item) if jsonable_encoder(item)[i] is not None}
    db.query(User).filter(User.id == id).update(update_item_encoded)

    db.commit()
    data = db.query(User).filter(User.id == id).first()
    return data

# Endpoints for Restaurant Details


@rest.get("/rest/all")
def rest_details(db: Session = Depends(get_db)):
    data = db.query(Restaurant).all()
    return {"data": data}


@rest.get("/rest/{id}")
def rest_by_id(id: int, db: Session = Depends(get_db)):

    data = db.query(Restaurant).filter(Restaurant.id == id).all()
    return {"data": data}


@rest.get("/rest/user/{id}")
def rest_by_id(id: int, db: Session = Depends(get_db)):

    data = db.query(Restaurant).filter(Restaurant.userid == id).all()
    return {"data": data}


@rest.post("/rest/", response_model=RestDetails)
def create_rest(detail_request: RestDetails, db: Session = Depends(get_db)):

    post = Restaurant()
    post.name = detail_request.name
    post.address = detail_request.address
    post.open_time = jsonable_encoder(detail_request.open_time)
    post.close_time = jsonable_encoder(detail_request.close_time)
    post.userid = detail_request.userid
    post.average_cost = detail_request.average_cost
    post.rating = detail_request.rating

    db.add(post)
    db.commit()
    return detail_request


@rest.delete("/rest/{id}")
def del_rest_by_id(id: int, db: Session = Depends(get_db)):

    db.query(Restaurant).filter(Restaurant.id == id).delete()
    db.commit()

    return {
        "code": "success",
        "message": "Restaurant details deleted from the database"}


@rest.put("/rest/{id}")
def update_rest(id: int, item: RestEdit, db: Session = Depends(get_db)):

    update_item_encoded = {i: jsonable_encoder(item)[i] for i in jsonable_encoder(
        item) if jsonable_encoder(item)[i] is not None}
    db.query(Restaurant).filter(
        Restaurant.id == id).update(update_item_encoded)

    db.commit()
    data = db.query(Restaurant).filter(Restaurant.id == id).first()
    return data

# Endpoints for Menu Category Details


@rest.get("/categ/all")
def category_details(db: Session = Depends(get_db)):
    data = db.query(Menu_Category).all()
    return {"data": data}


@rest.get("/categ/{id}")
def categ_by_id(id: int, db: Session = Depends(get_db)):

    data = db.query(Menu_Category).filter(Menu_Category.id == id).all()
    return {"data": data}


@rest.post("/categ/", response_model=CategDetails)
def create_user(detail_request: CategDetails, db: Session = Depends(get_db)):

    post = Menu_Category()
    post.name = detail_request.name
    post.description = detail_request.description
    post.restid = detail_request.restid

    db.add(post)
    db.commit()
    return detail_request


@rest.delete("/categ/{id}")
def del_categ_by_id(id: int, db: Session = Depends(get_db)):

    db.query(Menu_Category).filter(Menu_Category.id == id).delete()
    db.commit()

    return {
        "code": "success",
        "message": "Menu details deleted from the database"}


@rest.put("/categ/{id}")
def update_categ(id: int, item: CategEdit, db: Session = Depends(get_db)):

    update_item_encoded = {i: jsonable_encoder(item)[i] for i in jsonable_encoder(
        item) if jsonable_encoder(item)[i] is not None}
    db.query(Menu_Category).filter(
        Menu_Category.id == id).update(update_item_encoded)

    db.commit()
    data = db.query(Menu_Category).filter(Menu_Category.id == id).first()
    return data


# Endpoints for Menu Item Details

@rest.get("/item/all")
def item_details(db: Session = Depends(get_db)):
    data = db.query(Menu_Item).all()
    return {"data": data}


@rest.get("/item/{id}")
def item_by_name(id: int, db: Session = Depends(get_db)):

    data = db.query(Menu_Item).filter(Menu_Item.id == id).all()
    return {"data": data}


@rest.get("/item/categ/{id}")
def item_by_id(id: int, db: Session = Depends(get_db)):

    data = db.query(Menu_Item).filter(Menu_Item.categid == id).all()
    return {"data": data}


@rest.post("/item/", response_model=ItemDetails)
def create_item(detail_request: ItemDetails, db: Session = Depends(get_db)):

    post = Menu_Item()
    post.name = detail_request.name
    post.description = detail_request.description
    post.categid = detail_request.categid
    post.cost = detail_request.cost
    post.gluten_free = detail_request.gluten_free
    post.vegetarian = detail_request.vegetarian

    db.add(post)
    db.commit()
    return detail_request


@rest.delete("/item/{id}")
def del_item_by_id(id: int, db: Session = Depends(get_db)):

    db.query(Menu_Item).filter(Menu_Item.id == id).delete()
    db.commit()

    return {
        "code": "success",
        "message": "Item details deleted from the database"}


@rest.put("/item/{id}")
def update_item(id: int, item: ItemEdit, db: Session = Depends(get_db)):

    update_item_encoded = {i: jsonable_encoder(item)[i] for i in jsonable_encoder(
        item) if jsonable_encoder(item)[i] is not None}
    db.query(Menu_Item).filter(Menu_Item.id == id).update(update_item_encoded)

    db.commit()
    data = db.query(Menu_Item).filter(Menu_Item.id == id).first()
    return data


# Endpoints for Order Details

@rest.get("/order/all")
def item_details(db: Session = Depends(get_db)):
    data = db.query(Orders).all()
    return {"data": data}


@rest.get("/order/{id}")
def item_by_name(id: int, db: Session = Depends(get_db)):

    data = db.query(Orders).filter(Orders.id == id).all()
    return {"data": data}


@rest.post("/order/", response_model=OrderDetails)
def create_item(detail_request: OrderDetails, db: Session = Depends(get_db)):

    post = Orders()
    post.userid = detail_request.userid
    post.restid = detail_request.restid
    post.description = detail_request.description
    post.cost = detail_request.cost
    post.date = detail_request.date

    db.add(post)
    db.commit()
    return detail_request


@rest.delete("/order/{id}")
def del_item_by_id(id: int, db: Session = Depends(get_db)):

    db.query(Orders).filter(Orders.id == id).delete()
    db.commit()

    return {
        "code": "success",
        "message": "Item details deleted from the database"}


@rest.put("/order/{id}")
def update_item(id: int, item: OrderEdit, db: Session = Depends(get_db)):

    update_item_encoded = {i: jsonable_encoder(item)[i] for i in jsonable_encoder(
        item) if jsonable_encoder(item)[i] is not None}
    db.query(Orders).filter(Orders.id == id).update(update_item_encoded)

    db.commit()
    data = db.query(Orders).filter(Orders.id == id).first()
    return data
