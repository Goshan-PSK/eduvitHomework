age = input("Введите возраст")

if age.isdigit():
    age = int(age)
    if age >= 18:
        print("Совершеннолетний")
    else:
        print("Hесовершеннолетний")
elif age[0] == "-":
    print("Возраст не может быть отритцательным")
else:
    print("Ожидается число")