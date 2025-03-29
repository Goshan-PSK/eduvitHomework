age = input("Введите возраст")

if age.isdigit():
    age = int(age)
    if age >= 18:
        print("Совершеннолетний")
    else:
        print("Hесовершеннолетний")
elif age[0] == "-":
    print("Введи положительное число")
else:
    print("Введи число")