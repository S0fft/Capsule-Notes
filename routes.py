from fastapi import APIRouter, BackgroundTasks, HTTPException
from sqlalchemy.exc import NoResultFound

from celery_app import add_task
from repository import TaskRepository
from schemas import Task, TaskAdd

router = APIRouter(
    prefix='/tasks',
    tags=['Tasks']
)


@router.post('', response_model=Task)
async def post_task(task: TaskAdd, background_tasks: BackgroundTasks) -> Task:
    new_task = await TaskRepository.add_data(task)
    background_tasks.add_task(add_task.delay, task.name, task.description)

    return new_task


@router.get('')
async def get_tasks() -> list[Task]:
    tasks = await TaskRepository.get_data()

    return tasks


@router.get('/{task_id}', response_model=Task)
async def get_task_by_id(task_id: int) -> Task:
    task = await TaskRepository.get_task_by_id(task_id)

    return task


@router.put('/{task_id}', response_model=Task)
async def update_task(task_id: int, task_data: TaskAdd) -> Task:
    updated_task = await TaskRepository.update_data(task_id, task_data)

    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found!")

    return updated_task


@router.patch('/{task_id}', response_model=Task)
async def patch_task(task_id: int, task_data: TaskAdd) -> Task:
    try:
        updated_task = await TaskRepository.patch_data(task_id, task_data.dict(exclude_unset=True))
        return updated_task
    except NoResultFound:
        raise HTTPException(status_code=404, detail=f"Task with id {task_id} not found!")


@router.delete('/{task_id}')
async def delete_task(task_id: int):
    deleted = await TaskRepository.delete_data(task_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found!")

    return {"message": "Task deleted!"}
