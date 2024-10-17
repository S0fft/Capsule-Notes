from sqlalchemy import select

from database import TaskTable, new_session
from schemas import Task, TaskAdd


class TaskRepository:
    @classmethod
    async def add_data(cls, data: TaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskTable(**task_dict)
            session.add(task)

            await session.flush()
            await session.commit()

            return task.id

    @classmethod
    async def get_data(cls) -> list[Task]:
        async with new_session() as session:
            query = select(TaskTable)

            result = await session.execute(query)
            task_models = result.scalars().all()
            tasks_schemas = [Task.model_validate(task_model.__dict__) for task_model in task_models]

            return tasks_schemas
