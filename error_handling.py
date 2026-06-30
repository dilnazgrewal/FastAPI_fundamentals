class DuplicateTaskError(Exception):
    def __init__(self, title:str):
        self.title = title

next_id = 3

tasks = {
    1: "Books",
    2: "Milk"
}

def create_task(title: str):
    global next_id
    if title not in tasks.values():
        new_task = title
        tasks[next_id] = new_task
        return tasks
    else:
        raise DuplicateTaskError(title)

try:
    print(create_task("Milk"))

except DuplicateTaskError as e:
    print(f"{e.title} as a title already exists")

