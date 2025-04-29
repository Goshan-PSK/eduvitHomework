def myFunc(myList, number):
    result = []
    for x in myList:
        result.append(int(x) * number)
    return result


data = list(input("Введите список чисел через пробел: ").split(" "))
number = input("Введите множитель (по умолчанию 2): ")

if number == "":
    number = int(2)
else:
    number = int(number)

print("Результат функции",myFunc(data,number))

lambdaFunc = lambda arg1, arg2: map(myFunc, [arg1], [arg2])

print("Результат лямбда функции", list(lambdaFunc(data,number)))