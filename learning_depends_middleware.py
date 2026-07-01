from fastapi import FastAPI, Depends, HTTPException, Request
import time

app = FastAPI(title = "Finally understood Depends()")

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

def check_title(title: str):
    for value in tasks_db.values():
        if value["title"] == title:
            return value
    
    raise HTTPException(
        status_code=401, 
        detail= "Invalid title"
        )

@app.middleware("http")
async def calculate_time(request: Request, call_next):
    print("Started")
    start_time = time.time()
    process = await call_next(request)
    finish_time = time.time()
    processed_time = finish_time - start_time
    print("Finished")
    print(processed_time)
    return process

@app.put("/tasks/{title}")
def update_task(task: dict = Depends(check_title)):
    task["done"] = True
    return task