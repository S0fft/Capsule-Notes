import pytest
from httpx import AsyncClient

from database import create_tables, delete_tables
from main import app
from repository import TaskRepository
from schemas import TaskAdd


@pytest.fixture(scope="function")
async def setup_database():
    await delete_tables()
    await create_tables()

    yield

    await delete_tables()


@pytest.mark.asyncio
async def test_get_tasks(setup_database):
    task_data = TaskAdd(name="Test Task", description="This is a test task.")
    await TaskRepository.add_data(task_data)

    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "Test Task"
    assert response.json()[0]["description"] == "This is a test task."
