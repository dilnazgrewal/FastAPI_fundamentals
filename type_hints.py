from typing import List, Dict

# Integer
def square(num: int) -> int:
    return num * num

# Float
def calculate_area(radius: float) -> float:
    return 3.14159 * radius * radius

# String
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Boolean
def is_adult(age: int) -> bool:
    return age >= 18

# Optional (can be str or None)
def display_message(message: str | None = None) -> str:
    if message is None:
        return "No message provided."
    return message

# List
def total_marks(marks: list[int]) -> int:
    return sum(marks)


# Dictionary
def get_student() -> dict[str, int]:
    return {
        "Math": 90,
        "Science": 95
    }

# List of dictionaries
def get_employees() -> list[dict[str, str]]:
    return [
        {"name": "Alice", "department": "HR"},
        {"name": "Bob", "department": "IT"}
    ]

# No return value
def print_welcome(name: str) -> None:
    print(f"Welcome {name}!")

# Function call examples
print(square(5))
print(calculate_area(2.5))
print(greet("Dilnaz"))
print(is_adult(20))
print(display_message())
print(display_message("Learning FastAPI"))
print(total_marks([90, 85, 100]))
print(get_student())
print(get_employees())
print_welcome("Dilnaz")