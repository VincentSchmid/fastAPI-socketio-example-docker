from os import environ

import socketio
import uvicorn
from fastapi import FastAPI

app = FastAPI()
sio = socketio.AsyncServer(async_mode="asgi")
app = socketio.ASGIApp(sio)


@sio.on("connect", namespace="/test")
def handle_connect_analytic(sid, environ):
    print(f"client connected {sid}")


@sio.on("number", namespace="/test")
def on_message(sid, data):
    print(data)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(environ.get("PORT", 8070)),
    )
