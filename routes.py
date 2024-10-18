from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException

from repository import TaskRepository
from schemas import Task, TaskAdd, TaskId

router = APIRouter(
    prefix='/tasks',
    tags=['Tasks']
)


@router.post('', response_model=Task)
async def post_task(task: TaskAdd) -> Task:
    new_task = await TaskRepository.add_data(task)

    return new_task


@router.get('')
async def get_tasks() -> list[Task]:
    tasks = await TaskRepository.get_data()

    return tasks


@router.put('/{task_id}', response_model=Task)
async def update_task(task_id: int, task_data: TaskAdd) -> Task:
    updated_task = await TaskRepository.update_data(task_id, task_data)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task


@router.delete('/{task_id}')
async def delete_task(task_id: int):
    deleted = await TaskRepository.delete_data(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}
