import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Task(BaseModel):
    name: str
    description: str | None = None


@app.get('/tasks')
def get_tasks():
    task = Task(name='Create a new task!')

    return {'data': task}


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
