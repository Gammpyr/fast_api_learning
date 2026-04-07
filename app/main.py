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

fake_users = {
    1: {"username": "john_doe", "email": "john@example.com"},
    2: {"username": "jane_smith", "email": "jane@example.com"},
    3: {"username": "alice_jones", "email": "alice@example.com"},
    4: {"username": "bob_white", "email": "bob@example.com"},
}

fake_db = [{"username": "vasya", "user_info": "любит колбасу"}, {"username": "katya", "user_info": "любит петь"}]


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    if user_id in fake_users:
        return fake_users[user_id]
    return {"error": "User not found"}


@app.get("/users/")
async def read_users(username: str = None, email: str = None, limit: int = 10):
    filtered_users = fake_users

    if username:
        filtered_users = {
            key: user for key, user in filtered_users.items() if username.lower() in user["username"].lower()
        }

    if email:
        filtered_users = {key: user for key, user in filtered_users.items() if email.lower() in user["email"].lower()}

    return dict(list(filtered_users.items())[:limit])


# @app.post("/users")
# async def user_root(user: User):
#     is_adult = user.age >= 18
#
#     user_data = {"name": user.name, "age": user.age, "is_adult": is_adult}
#
#     return user_data


@app.get("/users")
async def get_all_users():
    return fake_db


@app.post("/add_user", response_model=User)
async def add_user(user: User):  # Используем модель для валидации данных
    fake_db.append({"username": user.username, "user_info": user.user_info})
    return user


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
