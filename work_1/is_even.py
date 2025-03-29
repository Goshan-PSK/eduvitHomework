number = input("Введите число:")

if number.isdigit():
    number = int(number)
    if number % 2 == 0:
        print(f"Число {number} является четным.")
    else:
        print(f"Число {number} является нечетным.")
else:
    print("Введи число")
    