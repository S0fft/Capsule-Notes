from database import TaskTable, new_session
from main import TaskAdd


class TaskRepository:
    @classmethod
    async def add_tasks(cls, data: TaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskTable(**task_dict)
            session.add(task)

            await session.flush()
            await session.commit()

            return task.id
