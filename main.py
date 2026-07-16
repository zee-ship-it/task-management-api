from fastapi import FastAPI
app = FastAPI()
 #def hello_server():
#   return  "Hello, server!"

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

