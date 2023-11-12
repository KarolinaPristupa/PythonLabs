#  Создать вручную и заполнить несколькими строками текстовый
# файл, в котором каждая строка будет содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Необходимо построчно прочитать файл, вычислить прибыль каждой
# компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт
# средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и
# их прибылями, а также словарь со средней прибылью. Если фирма получила
# убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий
# файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit":
# 2000}]
# Подсказка: использовать менеджер контекста.

import json

firm_data = []
profits = {}
average = {}
sum_profit = 0

with open("Фирмы.txt", encoding="utf-8") as f:
    for string in f:
        string = string.split()
        profit = int(string[2]) - int(string[3])
        if profit > 0:
            sum_profit += profit
            profits[string[0]] = profit

amount = len(profits)
average_profit = sum_profit/amount
average['average profit'] = average_profit
firm_data.append(profits)
firm_data.append(average)
print(firm_data)

with open("Фирмы.json", "w", encoding="utf-8") as firm:
    json.dump(firm_data, firm)
    