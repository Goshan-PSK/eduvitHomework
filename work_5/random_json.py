import string
import random
import json

firstNames = [
    "Liam", "Emma", "Noah", "Olivia", "Elijah", "Ava", "James", "Isabella", "William",
    "Sophia", "Benjamin", "Mia", "Lucas", "Charlotte", "Henry", "Amelia", "Alexander", "Harper"
]

lastNames = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez",
    "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore"
]

baseSymbols = string.ascii_uppercase + string.digits + string.punctuation

def genName():
    return f"{random.choice(firstNames)} {random.choice(lastNames)}"

def genPasswd():
    return ''.join(random.choices(baseSymbols, k=12))

def genMail(name):
    return name.replace(' ', '.') + "@example.com"

def genAge():
    return random.randint(18, 75)

def genJson(n):
    result = []
    for _ in range(n):
        name = genName()
        user = {
            "name": name,
            "age": genAge(),
            "email": genMail(name),
            "password": genPasswd()
        }
        result.append(user)
    return result

def save(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load(filename):
    with open(filename, 'r') as f:
        return json.load(f)

users = genJson(5)
save(users, 'users.json')
loaded = load('users.json')
print(json.dumps(loaded, indent=4))