from typing import Dict, List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


class Task(TaskCreate):
    id: int


tasks: Dict[int, Task] = {}
next_task_id = 1


@app.get("/health")
def health_check():
    # TODO: Return a JSON object indicating that the API is healthy.
    pass


@app.get("/tasks", response_model=List[Task])
def list_tasks():
    # TODO: Return every task in the collection.
    pass


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task_data: TaskCreate):
    global next_task_id
    # TODO: Create a task, assign its ID, store it, and return it.
    pass


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    # TODO: Return the requested task or raise an HTTP 404 error.
    pass


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_data: TaskCreate):
    # TODO: Replace the requested task or raise an HTTP 404 error.
    pass


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # TODO: Delete the requested task or raise an HTTP 404 error.
    pass