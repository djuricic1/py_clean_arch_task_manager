from fastapi import FastAPI

from task_manager.web.routers import task_router, user_router

app: FastAPI = FastAPI()
app.include_router(task_router)
app.include_router(user_router)
