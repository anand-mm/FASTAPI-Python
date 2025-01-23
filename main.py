from fastapi import FastAPI

from enum import Enum

app = FastAPI()


class ModelName(str,Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/details/{name}")
async def details(name: str):
    return {"message": f"Hello {name}"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    if q is None:
        return {"item_id": item_id}
    return {"item_id": item_id, "q": q}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

@app.get("/items")
async def read_item(limit: int, offset: int = 0):
    return {"limit": limit, "offset": offset}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None, short :bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item