import uvicorn
from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def index():
    return "你好"

@app.get("/users")
def users():

    return {"msg":"Get all","code":2001}

if __name__ == '__main__':
    uvicorn.run(app)