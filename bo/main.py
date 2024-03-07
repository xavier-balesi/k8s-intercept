#!/usr/bin/env python

import uvicorn
import os
from fastapi import FastAPI


app = FastAPI()

WHOAMI = os.getenv("WHOAMI", "remote")


@app.get("/")
def home():
    message = read_message()
    payload = {
        "message": message,
        "whoami": WHOAMI,
    }
    print(payload)
    return payload


def read_message():
    with open(os.path.join("/tmp", "message.txt")) as f:
        return f.read().strip()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
