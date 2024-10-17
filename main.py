from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import create_tables, delete_tables
from routes import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('All data from DB have been deleted!')

    await create_tables()
    print('Created a new empty tabels!')

    yield
    print('Shutdown')


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
