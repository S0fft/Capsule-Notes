from typing import Annotated

import uvicorn
from fastapi import Depends, FastAPI
from pydantic import BaseModel

app = FastAPI()


class TaskAdd(BaseModel):
    name: str
    description: str | None = None


class Task(TaskAdd):
    id: int


tasks = []


@app.post('/tasks')
async def add_task(task: Annotated[TaskAdd, Depends()]):
    return 'ok'


@app.get('/tasks')
def get_tasks():
    task = Task(name='Create a new task!')

    return {'data': task}


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
