from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
app = FastAPI()
@app.get("/")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }

@app.get("/health")
def health():
    return {"status": "ok"}

# In memory database
tasks = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Build CRUD API", "done": False},
    {"id": 3, "title": "Submit assignment", "done": False},
]

@app.get("/tasks")
def get_all_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_one_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail={"error": f"Task {task_id} not found"})


# Create
class TaskCreate(BaseModel):
    title: str


@app.post("/tasks")
def create_task(task: TaskCreate):
    # Validate input
    if not task.title or task.title.strip() == "":
        raise HTTPException(status_code=400, detail={"error": "Title is required and cannot be empty"})

    # Find next free ID
    next_id = max([t["id"] for t in tasks], default=0) + 1

    new_task = {
        "id": next_id,
        "title": task.title,
        "done": False
    }
    tasks.append(new_task)
    return new_task

# Stage 4: Update
class TaskUpdate(BaseModel):
    title: str | None = None
    done: bool | None = None

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            if updated.title is not None:
                if updated.title.strip() == "":
                    raise HTTPException(status_code=400, detail={"error": "Title cannot be empty"})
                task["title"] = updated.title
            if updated.done is not None:
                task["done"] = updated.done
            return task
    raise HTTPException(status_code=404, detail={"error": f"Task {task_id} not found"})


# Stage 4: Delete
@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            return  # Returns nothing
    raise HTTPException(status_code=404, detail={"error": f"Task {task_id} not found"})