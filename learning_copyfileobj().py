import shutil
from pathlib import Path

# Source file
source = Path("source.txt")

# Destination file
destination = Path("copied.txt")

# Open source in read mode and destination in write mode
with source.open("rb") as src:
    with destination.open("wb") as buffer:
        shutil.copyfileobj(src, buffer)

print("File copied successfully!")