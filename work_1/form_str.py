firstName = input("Введите ваше имя: ")
lastName = input("Введите вашу фамилию: ")
age = input("Введите ваш возраст: ")

fullName = "Ваше имя: {}, Фамилия: {}, Возраст: {} лет.".format(firstName, lastName, age)
print(fullName)


fullName = f"Ваше имя: {firstName}, Фамилия: {lastName}, Возраст: {age} лет."
print(fullName)