# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API for managing tasks with FastAPI. Practice defining endpoints, validating request data with Pydantic models, and returning appropriate HTTP responses.

## 📝 Tasks

### 🛠️ Create and run the FastAPI application

#### Descrição
Install the required packages, complete the health-check endpoint in `starter-code.py`, and start the development server.

```bash
python -m pip install fastapi uvicorn
uvicorn starter-code:app --reload
```

#### Requisitos
O programa concluído deve:

- Create a FastAPI application that can be started with the command above.
- Return `{"status": "ok"}` from `GET /health`.
- Make the interactive API documentation available at `/docs`.

### 🛠️ Create and retrieve tasks

#### Descrição
Use the provided Pydantic models and in-memory task store to implement endpoints for creating tasks and retrieving the task collection or an individual task.

#### Requisitos
O programa concluído deve:

- Accept a task with a `title` and an optional `completed` value, which defaults to `false`.
- Create a task with a unique integer `id` and return it from `POST /tasks` with status code `201`.
- Return all tasks from `GET /tasks` and a task by ID from `GET /tasks/{task_id}`.
- Return status code `404` when a requested task does not exist.

### 🛠️ Update and delete tasks

#### Descrição
Complete the remaining endpoints so clients can replace a task or remove it from the in-memory collection.

#### Requisitos
O programa concluído deve:

- Update a task with `PUT /tasks/{task_id}` and return the updated task.
- Delete a task with `DELETE /tasks/{task_id}` and return a confirmation response.
- Return status code `404` when an update or deletion targets a task that does not exist.
- Allow the endpoints to be tested through the interactive documentation at `/docs`.