from os import environ

import socketio
import uvicorn
from fastapi import FastAPI


app = FastAPI()
sio = socketio.Client()

MY_NAMESPACE = "/test"
DATA_EVENT_NAME = "number"
HANDLER_ADDRESS = (
    environ["HANDLER_ADDRESS"]
    if "HANDLER_ADDRESS" in environ
    else "http://0.0.0.0:8070"
)


@app.get("/connect")
def handle_connect():
    print(HANDLER_ADDRESS)
    sio.connect(HANDLER_ADDRESS, namespaces=[MY_NAMESPACE])
    return "..."


@app.get("/send/{message}")
def emit_number(message: str):
    print("starting sending messages")
    sio.emit(DATA_EVENT_NAME, message, namespace=MY_NAMESPACE)


@sio.event
def connect():
    print("connection success")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(environ.get("PORT", 8071)),
    )
