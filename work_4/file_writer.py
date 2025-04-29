def write(text, filename):

    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text + '\n')  

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            if (index + 1) % 2 == 0:
                print(line.strip())

write("Пример новой строки", "example.txt")