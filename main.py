from fastapi import FastAPI, HTTPException,status
from pydantic import BaseModel

app = FastAPI()

 #def hello_server():
#   return  f"Hello, server!"
class Createtask(BaseModel):
  title: str
  done:bool
## tasks
tasks=[
  { "id": 1, "title": "Go to gym","done":False },
  { "id": 2, "title": "Complete Assignment","done":True },
  { "id": 3, "title": "Read a book","done":False }
]

#1. GET "/"
@app.get("/")
def get_root():
  return {
    "name": "Task API",
    "version": "1.0",
    "endpoints": ["/tasks"]
  }

#2. GET "/health"
@app.get("/health")
def get_health():
  return {"status": "ok"}

#get /tasks
@app.get("/tasks")
def get_tasks():
  return tasks

#get id
@app.get("/tasks/{id}")
def get_single_task(id:int):
  for task in tasks:
    if task["id"] == id:
      return task
  raise HTTPException(status_code=404, detail=f"Task {id} not found!")

## Task creation 

@app.post("/tasks", status_code=status.HTTP_201_CREATED )
def create_task(task_inp: Createtask):
  if not task_inp.title:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title is required!")
  new_id= max(task["id"] for task in tasks) + 1 if tasks else 1
  new_task={"id": new_id, "title": task_inp.title, "done": False}
  tasks.append(new_task)
  return new_task

## Update task
@app.put("/tasks/{id}")
def update_task(id:int ,task_inp: Createtask):
  if not task_inp.title.strip():
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title is required!")
  for task in tasks:
    if task["id"] == id:
      task["title"] = task_inp.title
      task["done"] = task_inp.done
      return task
  raise HTTPException(status_code=404, detail=f"Task {id} not found!")

# Delete task
@app.delete("/tasks/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id:int):
  for task in tasks:
    if task["id"] == id:
      tasks.remove(task)
      return
  raise HTTPException(status_code=404, detail=f"Task {id} not found!")  