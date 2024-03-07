#!/usr/bin/env python

import os
import uvicorn
import requests
from fastapi import FastAPI

app = FastAPI()

BO_SVC = os.environ["BO_SVC"]
BO_PORT = os.environ["BO_PORT"]


@app.get("/")
def home():
    response = requests.get(f"http://{BO_SVC}:{BO_PORT}/").json()
    message = response["message"]
    whoisit = response["whoami"]
    return f"message from '{whoisit}' was '{message}'"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
