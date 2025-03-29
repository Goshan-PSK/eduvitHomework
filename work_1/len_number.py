while True:
    number = input("Введи число:")
    if (number.lstrip('-').isdigit()):
        r = len(number)
        print(f"В числе {len(number)} цифры")
    elif number == "exit":
        print("Выход ...")
        break
    else:
        print("Данные не число")
