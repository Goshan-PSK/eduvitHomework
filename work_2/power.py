data = input("Введите числа:")
power = int(input("Введите степень:"))
numbers = data.split(' ')

result = []

for number in numbers:
    if number.isdigit():
        number = int(number)
        number = pow(number, power)
    elif number[0] == '-':
        number = int(number.lstrip('-'))
        number = pow(number, power)
        if power % 2 != 0:
            number *= -1
    else:
        number = number * power
    result.append(number)
    

print("result:", result) 
