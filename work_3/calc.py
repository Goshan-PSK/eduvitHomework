import math

print("Доступные операции\n"
    "1. Сложение\n" \
    "2. Вычитание\n" \
    "3. Умножение\n" \
    "4. Деление\n" \
    "5. Возведение в степень\n" \
    "6. Факториал\n" \
    "7. Синус\n" \
    "8. Логарифм\n" \
    )

result = 0
while True:
    y = "0"
    op = input("Операция: ")
    if op == "exit":
        break
    if not op.isdigit():
        print("Invalid operation")
        continue
    elif int(op) > 8:
        print("Invalid operation")
        continue
    
    x = input("Число 1: ")
    if int(op) < 6:
        y = input("Число 2: ")
  
    if x.lstrip('-').replace('.','').isdigit() and y.lstrip('-').replace('.','').isdigit():
        x = float(x)
        y = float(y)
    else:
        # raise ValueError("some ex") // I think not good idea, but u want.
        print("Введи число")
        continue
    if op == "1":
        result = x + y
    elif op == "2":
        result = x - y
    elif op == "3":
        result = x * y
    elif op == "4":
        if y == 0:
            print("На ноль не делят")
            continue
        result = x / y
    elif op == "5":
        result = pow(x,y)
    elif op == "6":
        result = math.factorial(x)
    elif op == "7":
        result = math.sin(x)
    elif op == "8":
        result = math.log(x)

    print("Результат =", result)
