from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import TaskAdd

router = APIRouter(
    prefix='/tasks',
)


@router.post('')
async def add_task(task: Annotated[TaskAdd, Depends()]):
    task_id = await TaskRepository.add_data(task)

    return {'Ok!': True, 'task_id': task_id}


@router.get('')
async def get_tasks():
    tasks = await TaskRepository.find_all(tasks)

    return {'data': tasks}
