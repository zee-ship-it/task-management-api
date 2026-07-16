from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def hello_server():
  return  "Hello, server!"