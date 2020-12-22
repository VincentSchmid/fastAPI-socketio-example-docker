import random
from os import environ

import socketio
import uvicorn
from fastapi import FastAPI


class Model:
    def __init__(self):
        self.is_running = False

    def start(self):
        self.is_running = True

    def stop(self):
        self.is_running = False


app = FastAPI()
sio = socketio.Client()
model = Model()

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


@app.get("/start")
def emit_number():
    print("starting sending messages")
    model.start()
    while model.is_running:
        number = random.randint(0, 100)
        sio.emit(DATA_EVENT_NAME, number, namespace=MY_NAMESPACE)
        sio.sleep(1)


@app.get("/stop")
def emit_measurement():
    model.stop()
    return "stoped sending data"


@sio.event
def connect():
    print("connection success")


if __name__ == "__main__":
    sio.wait()
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(environ.get("PORT", 8071)),
        reload=True,
        debug=True,
    )
