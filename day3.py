##TASk A
#GET retrieves data (200 OK)
#POST creates new data (201 Created)
#PUT replaces an existing resource it updates the data
#PATCH partially updates a resource
#DELETE removes a resource (204 No Content)


#TASk B

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class item(BaseModel):
    name:str
    price:float

items = {1:{"name":"lap","price":200000},2:{"name":"bottle","price":250}}

@app.get("/items/{item_id}")
def get_item(item_id:int):
    return items.get(item_id,{"message":"item not found"})


@app.get("/items")
def get_items(limit: int = 10):
    return list(items.values())[:limit]



@app.post("/items", status_code=201)
def create_item(item: item):
    new_id = max(items.keys(), default=0) + 1
    items[new_id] = item.model_dump()
    return {"id": new_id, **items[new_id]}


#TASK C

from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)


#the pydantic Field is used to validate the input data min_length makes sure that the name is not empty and it has atleast one character and gt makes sure the value is greater than 1

#TASK D

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


# Response model includes the item's ID
class ItemResponse(Item):
    id: int


items = {
    1: {"name": "Laptop", "price": 50000},
    2: {"name": "Mouse", "price": 500},
}


@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    item = items.get(item_id)

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"id": item_id, **item}


@app.get("/items", response_model=list[Item])
def get_items(limit: int = 10):
    return list(items.values())[:limit]


@app.post("/items", response_model=ItemResponse, status_code=201)
def create_item(item: Item):
    new_id = max(items.keys(), default=0) + 1
    items[new_id] = item.model_dump()
    return {"id": new_id, **items[new_id]}


#task e
# im dont have much idea  about this concept so i was not able to finish this task
 