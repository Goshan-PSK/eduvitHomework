age = input("Введите возраст")

if age.isdigit():
    age = int(age)
    if age >= 18:
        print("Совершеннолетний")
    else:
        print("Hесовершеннолетний")
else:
    print("Введи положительное число.")