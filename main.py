from fastapi import FastAPI, HTTPException
app = FastAPI()
 #def hello_server():
#   return  f"Hello, server!"


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

#get /tasks-Return list
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