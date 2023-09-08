import uvicorn

if __name__ == "__main__":
    uvicorn.run("task_manager.app:app", host="0.0.0.0", port=80, reload=True)
