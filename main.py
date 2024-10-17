import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Task(BaseModel):
    name: str
    description: str | None


@app.get('/home')
def get_home():
    return 'Hello world!'


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
