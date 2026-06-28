import time
import asyncio

def cook_dish(name, seconds):
    print(f"Starting {name}")
    time.sleep(seconds)   # blocking — nothing else can happen during this
    print(f"{name} is done")

start = time.time()
cook_dish("Rice", 3)
cook_dish("Curry", 2)
cook_dish("Salad", 1)
print(f"Total time: {time.time() - start:.1f}s")

async def cook_dish(name, seconds):
    print(f"Starting {name}")
    await asyncio.sleep(seconds)   # non-blocking — event loop is free to do other things
    print(f"{name} is done")

async def main():
    start = time.time()
    # Start all three at once, and wait for all to finish
    await asyncio.gather(
        cook_dish("Rice", 3),
        cook_dish("Curry", 2),
        cook_dish("Salad", 1),
    )
    print(f"Total time: {time.time() - start:.1f}s")

asyncio.run(main())