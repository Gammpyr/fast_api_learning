from typing import Union

from fastapi import FastAPI
from fastapi.responses import FileResponse  # для отправки файлов
from pydantic import BaseModel

app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Авторелоад действительно работает"}

# @app.get("/")
# async def root():
#     return FileResponse("templates/index.html", # адрес шаблона
#                         filename="mainpage.html",  # имя загружаемого файла (страницы приеё загрузке)
#                         media_type="application/octet-stream") # автоматическая загрузка без отображения каких-нибудь интерпретируемых файлов

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.post('/calculate')
def calculate_nums(num1: int, num2: int):
    return {"calculated_nums": num1 + num2}

# class SNums(BaseModel):
#     num1: int
#     num2: int
#
# @app.post('/calculate')
# def calculate_nums(nums: SNums):
#     return {"calculated_nums": nums.num1 + nums.num2}
