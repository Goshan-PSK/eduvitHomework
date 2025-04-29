import math

squareNumber = [x**2 for x in range(1,11)]

days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
dayDict = {day: index + 1 for index, day in enumerate(days)}

sourceList = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
lowerList = [value.lower() for value in sourceList]

sourceNumbers = [1, 3, 4, 87, 98, 15, 7, 4]
evenNumber = [x for x in sourceNumbers if x % 2 == 0]

factDict = {x : math.factorial(x) for x in range(1,6)} 

print(squareNumber)
print(dayDict)
print(lowerList)
print(evenNumber)
print(factDict)