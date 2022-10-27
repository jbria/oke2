from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"Nada puede malir sal"}


@app.get("/name/{name}")
def hello_name(name: str):
    return {"Hello": name}
