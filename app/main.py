from fastapi import FastAPI, HTTPException,status
from pydantic import BaseModel
from app.repository import SqliteTaskRepository



app = FastAPI(
  title="Task Management API",
  description="With SQLITE",
  version="2.0"
)

repo= SqliteTaskRepository()

 #def hello_server():
#   return  f"Hello, server!"
class Createtask(BaseModel):
  title: str
  

class Updatetask(BaseModel):
  title: str
  done: bool

## in-memory database (tasks)
# tasks=[
#   { "id": 1, "title": "Go to gym","done":False },
#   { "id": 2, "title": "Complete Assignment","done":True },
#   { "id": 3, "title": "Read a book","done":False }
# ]

#1. GET "/"
@app.get("/")
def get_root():
  """Return API information."""
  return {
    "name": "Task API",
    "version": "2.0",
    "endpoints": ["/tasks"]
  }

#2. GET "/health"
@app.get("/health")
def get_health():
  """Return health check endpoint to verify the API is running."""
  return {"status": "ok"}

#get /tasks
@app.get("/tasks")
def get_tasks():
  """Return the list of all tasks."""
  return repo.get_all_tasks()

#get id
@app.get("/tasks/{id}")
def get_single_task(id:int):
  """Return a single task by its ID."""
  task= repo.get_by_id(id)
  if not task:
    raise HTTPException(status_code=404, detail=f"Task {id} not found!")
  return task


## Task creation 

@app.post("/tasks", status_code=status.HTTP_201_CREATED )
def create_task(task_inp: Createtask):
  """Create a new task with validation."""
  if not task_inp.title.strip():
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title is required!")
  return repo.create_task(task_inp.title)

## Update task
@app.put("/tasks/{id}")
def update_task(id:int ,task_inp: Updatetask):
  """Update an existing task by its ID with validation."""
  if not task_inp.title.strip():
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title is required!")
  updated_task= repo.update_task(id, task_inp.title, task_inp.done)
  if not updated_task:
    raise HTTPException(status_code=404, detail=f"Task {id} not found!")
  return updated_task

# Delete task
@app.delete("/tasks/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id:int):
  """Delete a task by its ID."""
  success= repo.delete_task(id)
  if not success:
    raise HTTPException(status_code=404, detail=f"Task {id} not found!")
  return 
