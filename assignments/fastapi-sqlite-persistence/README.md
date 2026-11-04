# 📘 Assignment: Persisting FastAPI Data with SQLite

## 🎯 Objective

Extend a FastAPI task API to store data in SQLite instead of keeping it only in memory. Practice creating a database table, using parameterized SQL queries, and preserving data between server restarts.

## 📝 Tasks

### 🛠️ Create the SQLite database table

#### Descrição
Complete the database initialization function in `starter-code.py` so the application creates a `tasks` table when it starts.

#### Requisitos
O programa concluído deve:

- Create a `tasks` table with an auto-incrementing integer `id`, a required text `title`, and an integer `completed` value that defaults to `0`.
- Use `CREATE TABLE IF NOT EXISTS` so restarting the server does not erase the table.
- Close the database connection after initialization.

### 🛠️ Persist task creation and retrieval

#### Descrição
Replace the in-memory behavior of the list, create, and get endpoints with SQLite queries.

#### Requisitos
O programa concluído deve:

- Insert new tasks and return the created task, including its database-generated ID.
- Return all saved tasks from `GET /tasks` and one task from `GET /tasks/{task_id}`.
- Use parameterized SQL queries with `?` placeholders for values received from requests.
- Return an HTTP `404` response when the requested task ID does not exist.

### 🛠️ Persist task updates and deletions

#### Descrição
Implement the update and delete endpoints using SQLite, then verify that task data remains available after restarting the development server.

#### Requisitos
O programa concluído deve:

- Update the title and completion status of an existing task.
- Delete an existing task and return a confirmation response.
- Return an HTTP `404` response when an update or deletion targets a missing task.
- Commit database changes and close each connection after use.
- Keep created and updated tasks available after the server is stopped and started again.