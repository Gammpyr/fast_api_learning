import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, world! app"}


my_awesome_api = FastAPI()


@my_awesome_api.get("/")
async def root():
    return {"message": "Hello, world! my_awesome_app"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=8000,
        reload=True
    )
