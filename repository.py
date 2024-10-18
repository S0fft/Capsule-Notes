from sqlalchemy import select

from database import TaskTable, new_session
from schemas import Task, TaskAdd


class TaskRepository:
    @classmethod
    async def add_data(cls, data: TaskAdd) -> Task:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskTable(**task_dict)
            session.add(task)

            await session.flush()
            await session.commit()

            return Task.model_validate(task.__dict__)

    @classmethod
    async def get_data(cls) -> list[Task]:
        async with new_session() as session:
            query = select(TaskTable)

            result = await session.execute(query)
            task_models = result.scalars().all()
            tasks_schemas = [Task.model_validate(task_model.__dict__) for task_model in task_models]

            return tasks_schemas

    @classmethod
    async def update_data(cls, task_id: int, data: TaskAdd) -> Task | None:
        async with new_session() as session:
            query = select(TaskTable).where(TaskTable.id == task_id)
            result = await session.execute(query)
            task_model = result.scalars().first()

            if not task_model:
                return None

            for key, value in data.model_dump().items():
                setattr(task_model, key, value)

            await session.commit()
            return Task.model_validate(task_model.__dict__)

    @classmethod
    async def delete_data(cls, task_id: int) -> bool:
        async with new_session() as session:
            query = select(TaskTable).where(TaskTable.id == task_id)
            result = await session.execute(query)
            task_model = result.scalars().first()

            if not task_model:
                return False

            await session.delete(task_model)
            await session.commit()
            return True
