from fastapi import FastAPI
from fastapi import Query
from enum import Enum

app = FastAPI(title="MY LEARNINGS")

tasks_db = {
    1: {
        "id": 1,
        "title": "Learn FastAPI",
        "priority": "high",
        "done": False
    },
    2: {
        "id": 2,
        "title": "Buy Groceries",
        "priority": "medium",
        "done": True
    },
    3: {
        "id": 3,
        "title": "Complete Python Assignment",
        "priority": "high",
        "done": False
    },
    4: {
        "id": 4,
        "title": "Watch a Movie",
        "priority": "low",
        "done": True
    },
    5: {
        "id": 5,
        "title": "Read FastAPI Documentation",
        "priority": "medium",
        "done": False
    }
}

next_id = 6

class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

@app.get("/tasks")
def list_tasks(
    search: str | None = None,
    priority: Priority | None = None
    ):
    if search is None and priority is None:
        return list(tasks_db.values())
    
    elif priority is not None:
        priority_list = []
        for value in tasks_db.values():
            if value["priority"] == priority.value:
                priority_list.append(value)
        return priority_list
        
    else:
        matches = []
        for value in tasks_db.values():
            if search.lower() in value["title"]:
                matches.append(value)
        return matches
    
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    return tasks_db.get(task_id, {"error": "not found"})

@app.post("/tasks")
def create_task(title: str, priority: Priority):
    global next_id
    task = {"id": next_id, "title": title, "priority": priority.value, "done": False}
    tasks_db[next_id] = task
    next_id += 1
    return task

@app.put("/tasks/{task_id}/complete")
def complete_task(task_id: int):
    tasks_db[task_id]["done"] = True
    return get_task(task_id)

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    deleted = tasks_db.pop(task_id, None)
    return {"deleted": deleted is not None}