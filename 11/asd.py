from fastapi import FastAPI

app = FastAPI()


def add(a , b):
    return a + b

@app.get("/add_by_get")
def add_get():
    c = add(1, 2)
    return {"c": c}

