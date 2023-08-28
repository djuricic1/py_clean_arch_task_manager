import uvicorn
from fastapi import FastAPI

from task_manager.web.app import rest_app

app: FastAPI = FastAPI()
app.mount("", rest_app)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=80, reload=True)
