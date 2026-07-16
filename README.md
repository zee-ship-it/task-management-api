# Task Management CRUD API 

A robust, lightweight in-memory CRUD API built using **Python** and **FastAPI** to manage a simple to-do list. 

##  Features
- **Full CRUD Support**: Create, Read, Update, and Delete tasks seamlessly.
- **Strict Data Validation**: Prevents empty/invalid task titles with proper HTTP 400 status codes.
- **Automatic Documentation**: Built-in interactive API testing via Swagger UI.
- **In-Memory Storage**: Data persists in the application memory during runtime.

---

##  Tech Stack & Tools
- **Language**: Python 3.10+
- **Framework**: FastAPI
- **Web Server**: Uvicorn
- **API Documentation**: Swagger UI

---

##  How to Install and Run Locally

Follow these quick steps to run the server on your machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/zee-ship-it/task-management-api.git](https://github.com/zee-ship-it/task-management-api.git)
cd task-management-api
2. Install DependenciesMake sure you have FastAPI and Uvicorn installed:Bashpip install fastapi uvicorn
3. Run the ServerStart the Uvicorn ASGI server with the reload flag enabled:Bashuvicorn main:app --reload
The server will start running at http://127.0.0.1:8000.📊 API Endpoints TableMethodEndpointDescriptionStatus CodeGET/Retrieve API metadata and description.200 OKGET/healthHealth check to verify if the server is running.200 OKGET/tasksRetrieve the complete list of tasks.200 OKGET/tasks/{id}Retrieve a single task by its unique ID.200 OK / 404POST/tasksCreate a new task (Requires validation).201 Created / 400PUT/tasks/{id}Update an existing task's title/completion status.200 OK / 400 / 404DELETE/tasks/{id}Delete a task by its unique ID.204 No Content / 404🧪 Terminal Testing (curl output)Here is a sample output of retrieving the list of tasks via terminal using curl:Bashcurl -i [http://127.0.0.1:8000/tasks](http://127.0.0.1:8000/tasks)

Response:JSONHTTP/1.1 200 OK
date: Thu, 16 Jul 2026 16:55:00 GMT
server: uvicorn
content-length: 198
content-type: application/json

[
  {"id": 1, "title": "Go to gym", "done": false},
  {"id": 2, "title": "Complete Assignment", "done": true},
  {"id": 3, "title": "Read a book", "done": false}
]