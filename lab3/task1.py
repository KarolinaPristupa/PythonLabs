# Создать программный файл F1 в текстовом формате, записать в него
# построчно данные, вводимые пользователем. Об окончании ввода данных
# будет свидетельствовать пустая строка. Создать текстовый файл F1 не менее,
# чем из 10 строк и записать в него информацию. Скопировать в файл F2
# только строки из F1, которые не содержат цифр. –

with open("F1.txt", "w") as f1:
    for i in range(1, 10):
        string = input(f"Введите строку {i}: ")
        if not string:
            break
        f1.write(string + "\n")


print("На данный момент в файле F1 содержатся строки: \n")
with open("F1.txt", "r") as f1, open("F2.txt", "w") as f2:
        for line in f1:
            print(line.strip())
            if not any(char.isdigit() for char in line):
                f2.write(line)

print("\nНа данный момент в файле F2 содержатся строки: \n")
with open("F2.txt", "r") as f2:
    for line2 in f2:
        print(line2.strip())