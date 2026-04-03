import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

from app.config import load_config
from app.logger import logger
from app.models.user_models import User

app = FastAPI()

config = load_config()

if config.debug:
    app.debug = True
else:
    app.debug = False


@app.post("/users")
async def user_root(user: User):
    is_adult = user.age >= 18

    user_data = {"name": user.name, "age": user.age, "is_adult": is_adult}

    return user_data


@app.post("/calculate")
async def addition(num1: int, num2: int = 0):
    return {"result": num1 + num2}


@app.get("/")
async def read_root():
    logger.info("Handling request to root endpoint")
    return {"message": "Hello World!"}


@app.get("/index")
async def temp_root():
    return FileResponse("../templates/index.html")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
