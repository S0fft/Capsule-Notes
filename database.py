from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine(
    'sqlite+aiosqlite:///tasks.db'
)
new_session = async_sessionmaker(engine, expire_on_commit=False)


class BaseModel(DeclarativeBase):
    pass


class TaskTable(BaseModel):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str | None] = None


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)
