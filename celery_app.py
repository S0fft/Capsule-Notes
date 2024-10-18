from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')


@app.task
def add_task(name: str, description: str):
    if not name:
        raise ValueError("Task name cannot be empty!")

    print(f"Task added: {name}, Description: {description}")
