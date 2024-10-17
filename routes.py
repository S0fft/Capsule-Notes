from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import Task, TaskAdd, TaskId

router = APIRouter(
    prefix='/tasks',
    tags=['Tasks']
)


@router.post('')
async def post_task(task: Annotated[TaskAdd, Depends()]) -> TaskId:
    task_id = await TaskRepository.add_data(task)

    return {'Ok!': True, 'task_id': task_id}


@router.get('')
async def get_tasks() -> list[Task]:
    tasks = await TaskRepository.get_data()

    return tasks
