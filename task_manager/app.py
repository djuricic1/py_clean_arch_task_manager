import uvicorn
from fastapi import FastAPI

from task_manager.web.routers import task_router, user_router

app: FastAPI = FastAPI()
app.include_router(task_router)
app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=80, reload=True)
