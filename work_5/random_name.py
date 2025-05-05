import random
import string
from pathlib import Path

for _ in range(10):
    symbols = string.ascii_letters + string.digits
    fileName = ""
    for _ in range(8):
        fileName += random.choice(symbols)
    fileName +=".txt"
    file = Path(fileName)
    file.touch()
    print(file.absolute())