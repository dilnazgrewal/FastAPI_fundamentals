from fastapi import FastAPI, HTTPException

app = FastAPI()

users = {
    1: {"name": "Dilnaz", "role": "admin"},
    2: {"name": "Sehajnoor", "role": "user"}
}

# 404 Not Found example

@app.get("/user/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]


# 403 Forbidden example

@app.get("/admin/{user_id}")
def admin_panel(user_id: int):
    user = users.get(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Access denied: Admin only")

    return {"message": "Welcome admin panel"}

# 400 Bad Request example

@app.get("/divide")
def divide(a: int, b: int):
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")

    return {"result": a / b}

# 401 Unauthorized example

@app.get("/secure-data")
def secure_data(api_key: str | None = None):
    if api_key is None:
        raise HTTPException(status_code=401, detail="API key required")

    if api_key != "secret123":
        raise HTTPException(status_code=401, detail="Invalid API key")

    return {"data": "Sensitive information"}

# General validation example

@app.post("/age-check")
def check_age(age: int):
    if age < 0:
        raise HTTPException(status_code=400, detail="Age cannot be negative")

    if age < 18:
        raise HTTPException(status_code=403, detail="Must be 18+")

    return {"message": "Allowed"}