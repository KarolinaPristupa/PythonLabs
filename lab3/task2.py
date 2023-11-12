# Создать текстовый файл (не программно). Построчно записать
# фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад более 2 тысяч, вывести
# фамилии этих сотрудников. Вывести на экран сотрудников с минимальным
# окладом.

with open("Employees (t2).txt", encoding="utf-8") as f:
    print("+--------------+---------+")
    print("|   Фамилия    |  Оклад  |")
    print("+--------------+---------+")
    strings = f.readlines()
    for string in strings:
        record = string.split()
        format_text = f"{record[0]:<14}| {record[1]:<8}"
        print(f"|{format_text}|")
    print("+--------------+---------+")
    print("\nСотрудники с окладами > 2000: \n")
    for line in strings:
        new_record = line.split()
        if int(new_record[1]) > 2000:
            print(new_record[0])
