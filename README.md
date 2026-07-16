# Task Management CRUD API

A robust and lightweight in-memory CRUD API built using Python and FastAPI to manage a simple to-do list. This project was developed as part of the FlyRank Internship Backend Track for Week Two, Assignment AOne.

## Features
- Full CRUD Support: Create, Read, Update, and Delete tasks seamlessly.
- Input Data Validation: Prevents empty or invalid task titles, returning proper HTTP Bad Request status codes.
- Automatic Documentation: Interactive API testing and visualization via Swagger UI.
- In-Memory Storage: Data persists in the application memory during runtime, utilizing a structured Python list of dictionaries as a temporary database.

---

## Tech Stack and Tools
- Language: Python
- Framework: FastAPI
- Web Server: Uvicorn
- API Documentation: Swagger UI
- Version Control: Git and GitHub

---

## How to Install and Run Locally

Follow these steps to run the server on your local machine:

### Clone the Repository
```bash
git clone [https://github.com/zee-ship-it/task-management-api.git](https://github.com/zee-ship-it/task-management-api.git)
cd task-management-api
Install DependenciesEnsure you have FastAPI and Uvicorn installed on your system:Bashpip install fastapi uvicorn
Run the ServerStart the Uvicorn ASGI server with the reload flag enabled to monitor code changes:Bashuvicorn main:app --reload
The server will start running locally at the localhost address on port eight thousand.API Endpoints TableMethodEndpointDescriptionExpected Status CodeGET/Retrieve API metadata and description.OKGET/healthHealth check to verify if the server is running.OKGET/tasksRetrieve the complete list of tasks.OKGET/tasks/{id}Retrieve a single task by its unique ID.OK / Not FoundPOST/tasksCreate a new task (Requires input validation).Created / Bad RequestPUT/tasks/{id}Update an existing task's title or completion status.OK / Bad Request / Not FoundDELETE/tasks/{id}Delete a task by its unique ID.No Content / Not FoundTerminal Testing (curl Output Example)Below is a sample terminal output when retrieving the list of tasks using curl:Bashcurl -i [http://127.0.0.1:8000/tasks](http://127.0.0.1:8000/tasks)
Response:JSONHTTP/1.1 OK
date: Thu, 16 Jul 2026 17:05:00 GMT
server: uvicorn
content-length: 198
content-type: application/json

[
  {"id": 1, "title": "Go to gym", "done": false},
  {"id": 2, "title": "Complete Assignment", "done": true},
  {"id": 3, "title": "Read a book", "done": false}
]
Swagger UI Interactive DocumentationBelow is the screenshot of the interactive API documentation interface available locally at the docs endpoint:
