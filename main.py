
from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.expression import null
import DB_Models
from Models import *
from DB_Models import *
from fastapi import FastAPI, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from DB_Models import Orders, User, Restaurant, Inventory, Wishlist
from DB_Models.Orders.orders import *
from DB_Models.Inventory.inventory import *
from DB_Models.Menu.menu import *
from DB_Models.Wishlist.wishlist import *
from DB_Models.User.user import *
from Models.Order.order import *
from Models.Menu.menu import *
from Models.User.user import *
from Models.Inventory.inventory import *
from Models.Restaurant.restaurant import *
from Models.Wishlist.wishlist import *
from DB_Models.database import SessionLocal, engine
from passlib.context import CryptContext
from datetime import datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlite3 import Connection as SQLite3Connection
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


@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

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

    if db.query(User).filter(User.id == id):
        db.query(User).filter(User.id == id).delete()
        db.commit()
        return {
            "code": "success",
            "message": "User details deleted from the database"}
    else:
        return "No such User ID"


@rest.put("/user/{id}")
def update_user(id: int, item: UserEdit, db: Session = Depends(get_db)):

    update_item_encoded = {i: jsonable_encoder(item)[i] for i in jsonable_encoder(
        item) if jsonable_encoder(item)[i] is not None}
    db.query(User).filter(User.id == id).update(update_item_encoded)

    db.commit()
    data = db.query(User).filter(User.id == id).first()
    if data:
        return data
    else:
        return "No such used id exists"


@rest.get("/user/totalspent/{id}")
def total_spent(id: int, db: Session = Depends(get_db)):

    a = [
        i[0] for i in db.query(
            Menu_Item.cost).filter(
            Menu_Item.id == Orders.itemid).all()]
    b = [
        i[0] for i in db.query(
            Orders.quantity).filter(
            Orders.userid == id).all()]
    return "The total amount spent is : " + \
        str(sum(x * y for x, y in zip(a, b)))


@rest.get("/user/orderhistory/{id}")
def order_history(id: int, db: Session = Depends(get_db)):

    history = [("Order Id", "Date")]
    values = [(i[0], i[1].strftime('%m/%d/%Y'))
              for i in db.query(Orders.id, Orders.date).filter(Orders.userid == id).all()]
    history.extend(values)

    return history

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
    post.open_time = detail_request.open_time
    post.close_time = detail_request.close_time
    post.userid = detail_request.userid
    post.average_cost = detail_request.average_cost
    post.rating = detail_request.rating

    db.add(post)
    db.commit()
    return detail_request


@rest.delete("/rest/{id}")
def del_rest_by_id(id: int, db: Session = Depends(get_db)):

    if db.query(Restaurant).filter(Restaurant.id == id):
        db.query(Restaurant).filter(Restaurant.id == id).delete()
        db.commit()
        return {
            "code": "success",
            "message": "Restaurant details deleted from the database"}
    else:
        return "No such Restaurant ID"


@rest.put("/rest/{id}")
def update_rest(id: int, item: RestEdit, db: Session = Depends(get_db)):

    update_item_encoded = {i: jsonable_encoder(item)[i] for i in jsonable_encoder(
        item) if jsonable_encoder(item)[i] is not None}
    db.query(Restaurant).filter(
        Restaurant.id == id).update(update_item_encoded)

    db.commit()
    data = db.query(Restaurant).filter(Restaurant.id == id).first()
    if data:
        return data
    else:
        return "No such restaurant id exists"

# Endpoints for Menu Category Details


@rest.get("/categ/all")
def category_details(db: Session = Depends(get_db)):
    data = db.query(Menu_Category).all()
    return {"data": data}


@rest.get("/categ/{id}")
def category_by_id(id: int, db: Session = Depends(get_db)):

    data = db.query(Menu_Category).filter(Menu_Category.id == id).all()
    return {"data": data}


@rest.post("/categ/")
def create_category(
        detail_request: CategDetails,
        db: Session = Depends(get_db)):

    if not db.query(Menu_Category).filter(
            Menu_Category.name == detail_request.name).filter(
            Menu_Category.restid == detail_request.restid).first():
        post = Menu_Category()
        post.name = detail_request.name
        post.description = detail_request.description
        post.restid = detail_request.restid

        db.add(post)
        db.commit()
        return detail_request
    else:
        return "Data already exists for given inputs"


@rest.delete("/categ/{id}")
def del_category_by_id(id: int, db: Session = Depends(get_db)):

    if db.query(Menu_Category).filter(Menu_Category.id == id):
        db.query(Menu_Category).filter(Menu_Category.id == id).delete()
        db.commit()
        return {
            "code": "success",
            "message": "Menu Category details deleted from the database"}
    else:
        return "No such Category ID"


@rest.put("/categ/{id}")
def update_category(id: int, item: CategEdit, db: Session = Depends(get_db)):

    update_item_encoded = {i: jsonable_encoder(item)[i] for i in jsonable_encoder(
        item) if jsonable_encoder(item)[i] is not None}
    db.query(Menu_Category).filter(
        Menu_Category.id == id).update(update_item_encoded)

    db.commit()
    data = db.query(Menu_Category).filter(Menu_Category.id == id).first()
    if data:
        return data
    else:
        return "No such category id exists"


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


@rest.post("/item/")
def create_item(detail_request: ItemDetails, db: Session = Depends(get_db)):

    if not db.query(Menu_Item).filter(
            Menu_Item.name == detail_request.name).filter(
            Menu_Item.categid == detail_request.categid).first():

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
    else:
        return "Data already exists for the given inputs"


@rest.delete("/item/{id}")
def del_item_by_id(id: int, db: Session = Depends(get_db)):

    if db.query(Menu_Item).filter(Menu_Item.id == id):
        db.query(Menu_Item).filter(Menu_Item.id == id).delete()
        db.commit()
        return {
            "code": "success",
            "message": "Menu Item details deleted from the database"}
    else:
        return "No such Menu Item ID"


@rest.put("/item/{id}")
def update_item(id: int, item: ItemEdit, db: Session = Depends(get_db)):

    update_item_encoded = {i: jsonable_encoder(item)[i] for i in jsonable_encoder(
        item) if jsonable_encoder(item)[i] is not None}
    db.query(Menu_Item).filter(Menu_Item.id == id).update(update_item_encoded)

    db.commit()
    data = db.query(Menu_Item).filter(Menu_Item.id == id).first()
    if data:
        return data
    else:
        return "No such item id exists"


# Endpoints for Order Details

@rest.get("/order/all")
def order_details(db: Session = Depends(get_db)):
    data = db.query(Orders).all()
    return {"data": data}


@rest.get("/order/{id}")
def order_by_name(id: int, db: Session = Depends(get_db)):

    data = db.query(Orders).filter(Orders.id == id).all()
    return {"data": data}


@rest.post("/order/")
def create_order(detail_request: OrderDetails, db: Session = Depends(get_db)):

    post = Orders()
    post.userid = detail_request.userid
    post.restid = detail_request.restid
    post.description = detail_request.description
    post.quantity = detail_request.quantity
    post.date = detail_request.date
    post.itemid = detail_request.itemid

    if(db.query(Inventory.quantity).filter(Inventory.itemid == detail_request.itemid).first() is not None and
       db.query(Inventory.quantity).filter(Inventory.restaurantid == detail_request.restid).first() is not None):

        if(db.query(Inventory.quantity).filter(Inventory.itemid == detail_request.itemid)
           .filter(Inventory.restaurantid == detail_request.restid).first()[0] >= detail_request.quantity):
            db.add(post)

            newquantity = db.query(
                Inventory.quantity).filter(
                Inventory.itemid == detail_request.itemid).filter(
                Inventory.restaurantid == detail_request.restid).first()[0] - detail_request.quantity
            db.query(Inventory).filter(Inventory.itemid == detail_request.itemid).filter(
                Inventory.restaurantid == detail_request.restid).update({"quantity": newquantity})
            db.commit()
            return detail_request
        else:
            return "Not enough inventory to make that order"

    else:
        return "Not enough inventory to make that order"


@rest.delete("/order/{id}")
def del_order_by_id(id: int, db: Session = Depends(get_db)):

    if db.query(Orders).filter(Orders.id == id):
        db.query(Orders).filter(Orders.id == id).delete()
        db.commit()
        return {
            "Code": "Success",
            "Message": "Order details deleted from the database"}
    else:
        return "No such Order ID"


@rest.put("/order/{id}")
def update_order(id: int, item: OrderEdit, db: Session = Depends(get_db)):

    update_item_encoded = {i: jsonable_encoder(item)[i] for i in jsonable_encoder(
        item) if jsonable_encoder(item)[i] is not None}
    db.query(Orders).filter(Orders.id == id).update(update_item_encoded)

    db.commit()
    data = db.query(Orders).filter(Orders.id == id).first()
    if data:
        return data
    else:
        return "No such order id exists"


# Endpoints for Inventory Details


@rest.get("/inventory/all")
def inventory_details(db: Session = Depends(get_db)):
    data = db.query(Inventory).all()
    return {"data": data}


@rest.get("/inventory/{id}")
def inventory_by_id(id: int, db: Session = Depends(get_db)):

    data = db.query(Inventory).filter(Inventory.id == id).all()
    return {"data": data}


@rest.post("/inventory/")
def create_inventory(
        detail_request: InventoryDetails,
        db: Session = Depends(get_db)):

    if not db.query(Inventory).filter(
            Inventory.itemid == detail_request.itemid).filter(
            Inventory.restaurantid == detail_request.restaurantid).first():

        post = Inventory()
        # post.name = detail_request.name
        post.quantity = detail_request.quantity
        post.itemid = detail_request.itemid
        post.restaurantid = detail_request.restaurantid

        db.add(post)
        db.commit()
        return detail_request

    else:
        return "Data already exists for given inputs"


@rest.delete("/inventory/{id}")
def del_inventory_by_id(id: int, db: Session = Depends(get_db)):

    if db.query(Inventory).filter(Inventory.id == id):
        db.query(Inventory).filter(Inventory.id == id).delete()
        db.commit()
        return {
            "Code": "Success",
            "Message": "Inventory details deleted from the database"}
    else:
        return "No such Inventory ID"


@rest.put("/inventory/{id}")
def update_inventory(
        id: int,
        item: InventoryEdit,
        db: Session = Depends(get_db)):

    update_item_encoded = {i: jsonable_encoder(item)[i] for i in jsonable_encoder(
        item) if jsonable_encoder(item)[i] is not None}
    db.query(Inventory).filter(Inventory.id == id).update(update_item_encoded)

    db.commit()
    data = db.query(Inventory).filter(Inventory.id == id).first()
    if data:
        return data
    else:
        return "No such inventory id exists"


# Endpoints for Wishlist Details


@rest.get("/wishlist/all")
def wishlist_details(db: Session = Depends(get_db)):
    data = db.query(Wishlist).all()
    return {"data": data}


@rest.get("/wishlist/{id}")
def wishlist_by_id(id: int, db: Session = Depends(get_db)):

    data = db.query(Wishlist).filter(Wishlist.id == id).all()
    return {"data": data}


@rest.post("/wishlist/", response_model=WishlistDetails)
def create_wishlist(
        detail_request: WishlistDetails,
        db: Session = Depends(get_db)):

    post = Wishlist()
    post.name = detail_request.name
    post.description = detail_request.description
    post.no_of_votes = detail_request.no_of_votes
    post.categoryid = detail_request.categoryid

    db.add(post)
    db.commit()
    return detail_request


@rest.delete("/wishlist/{id}")
def del_wishlist_by_id(id: int, db: Session = Depends(get_db)):

    if db.query(Wishlist).filter(Wishlist.id == id):
        db.query(Wishlist).filter(Wishlist.id == id).delete()
        db.commit()
        return {
            "Code": "Success",
            "Message": "Wishlist details deleted from the database"}
    else:
        return "No such Wish list ID"


@rest.put("/wishlist/{id}")
def update_wishlist(
        id: int,
        item: WishlistEdit,
        db: Session = Depends(get_db)):

    update_item_encoded = {i: jsonable_encoder(item)[i] for i in jsonable_encoder(
        item) if jsonable_encoder(item)[i] is not None}
    db.query(Wishlist).filter(Wishlist.id == id).update(update_item_encoded)

    db.commit()
    data = db.query(Wishlist).filter(Wishlist.id == id).first()
    if data:
        return data
    else:
        return "No such wishlist id exists"
