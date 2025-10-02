<b>Lesson 3 Backend</b>

<b>Overview:</b>
This folder contains a Node.js backend with a local SQLite database (`SininDatabase.db`).  
- Provides RESTful API endpoints for simulated sensor data and user management.  
- Demonstrates CRUD operations (read and create) with SQLite.  

<b>Files:</b>
- **server.js** &mdash; Node.js Express server connecting to SQLite database and exposing API endpoints.  
- **SininDatabase.db** &mdash; SQLite database file storing user information.  
- **package.json** &mdash; Node.js project configuration.  
- **package-lock.json** &mdash; Lock file for dependencies.  
- **node_modules/** &mdash; Installed Node.js dependencies (do not modify manually).

<b>How it works:</b>
- Creates a `users` table if it does not exist, with fields:
  - `id` (INTEGER PRIMARY KEY AUTOINCREMENT)  
  - `name` (TEXT, NOT NULL)  
  - `email` (TEXT, NOT NULL, UNIQUE)
- Provides three endpoints:
  1. `GET /api/sensor` – Returns simulated temperature and humidity JSON.  
  2. `GET /api/users` – Returns all users in the database.  
  3. `POST /api/users` – Adds a new user with `name` and `email` in the request body.

<b>Example JSON response from `GET /api/sensor`:</b>

```json
{
  "temperature": 22.5,
  "humidity": 55,
  "status": "OK"
}
```
