import sqlite3
from contextlib import closing
from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

DATABASE_PATH = "tasks.db"
app = FastAPI()


class TaskInput(BaseModel):
    title: str
    completed: bool = False


class Task(TaskInput):
    id: int


def connect_to_database():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


@app.on_event("startup")
def initialize_database():
    with closing(connect_to_database()) as connection:
        # TODO: Create the tasks table if it does not already exist.
        pass


@app.get("/tasks", response_model=List[Task])
def list_tasks():
    with closing(connect_to_database()) as connection:
        # TODO: Select all rows and return them as Task objects.
        pass


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task_data: TaskInput):
    with closing(connect_to_database()) as connection:
        # TODO: Insert the task, commit the change, and return the saved row.
        pass


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    with closing(connect_to_database()) as connection:
        # TODO: Select the task by ID or raise HTTPException with status 404.
        pass


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_data: TaskInput):
    with closing(connect_to_database()) as connection:
        # TODO: Update the task, commit the change, and return the saved row.
        pass


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    with closing(connect_to_database()) as connection:
        # TODO: Delete the task, commit the change, or raise HTTPException with status 404.
        pass