# Сформировать (не программно) текстовый файл. В нём каждая
# строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету. Сюда должно входить и
# количество занятий. Необязательно, чтобы для каждого предмета были все
# типы занятий.
# Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести его на экран.

subjects = {}
with open("Предметы.txt", "r", encoding="utf-8") as f:
    print("+-------------------+-----+-----+-----+")
    print("|    Дисциплина     |  ЛР |  ПЗ |  ЛР |")
    print("+-------------------+-----+-----+-----+")
    strings = f.readlines()
    for string in strings:
        record = string.split()
        format_text = f"{record[0]:<19}|  {int(record[1][:-3]):<3}|  {int(record[2][:-4]):<3}|  {int(record[3][:-4]):<3}"
        print(f"|{format_text}|")
        print("+-------------------+-----+-----+-----+")
        amount = int(record[1][:-3]) + int(record[2][:-4]) + int(record[3][:-4])
        subjects[record[0]] = amount

print(subjects)
