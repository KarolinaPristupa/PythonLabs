# Напишите функцию, которая будет принимать один аргумент.

def define_the_type(some_type):
    if isinstance(some_type, list):
        return sum_between_first_two(some_type)
    elif isinstance(some_type, tuple):
        return change_elements(some_type)
    elif isinstance(some_type, int):
        return even_sum(some_type)
    elif isinstance(some_type, str):
        return translate_characters(some_type)
    else:
        return "Ошибка: Неподдерживаемый тип данных!"


# Если в функцию передаётся список, Найдите сумму элементов между двумя первыми нулями.
def sum_between_first_two(some_type):
    try:
        first_zero = some_type.index(0)
        second_zero = some_type.index(0, first_zero+1)
        lst = some_type[first_zero+1: second_zero]
        result = sum(lst)
        print(f"Вы ввели список. Индекс первого нулевого элемента - {first_zero}")
        print(f"                 Индекс второго нулевого элемента - {second_zero}")
        print(f"Сумма элементов между ними: {result}")
    except ValueError:
        return "Ошибка: Не найдены два нуля в списке!"


# Если кортеж, найти максимальный и минимальный элементы. Поменять их местами.
def change_elements(some_type):
    if len(some_type) < 2:
        return print("Ошибка. В кортеже меньше 2-ух элементов!")
    print(f"Вы ввели кортеж")
    print(f"Кортеж до:    {some_type}")
    max_el = max(some_type)
    min_el = min(some_type)
    in_max = some_type.index(max_el)
    in_min = some_type.index(min_el)
    some_type = list(some_type)
    some_type[in_max], some_type[in_min] = some_type[in_min], some_type[in_max]
    result = tuple(some_type)
    print(f"Кортеж после: {result}")


# Число – найти сумму четных цифр.
def even_sum(number):
    if number < 0:
        number = abs(number)
    if number < 10:
        return print("Ошибка: Число слишком маленькое!")
    num_str = str(number)
    even_digit_sum = sum(int(digit) for digit in num_str if int(digit) % 2 == 0)
    print(f"Вы ввели число")
    print(f"Четные цифры: ")
    for digit in num_str:
        if int(digit) % 2 == 0:
            print(f"      {int(digit)}")
    print(f"Сумма четных цифр: {even_digit_sum}")


# Строка – каждый символ перевести в соответствующий ему код из таблицы символов Unicode.
def translate_characters(s):
    print(f"Вы ввели строку")
    strl = list(s)
    for i in strl:
        print(f"Коды символа {i}: {ord(i)}")


while True:
    user_data = input("Введите данные(или !, чтобы выйти): ")
    if user_data == '!':
        break
    try:
        user_data = eval(user_data)
    except(ValueError, SyntaxError, NameError):
        user_data_eval = None

    define_the_type(user_data)
    if isinstance(user_data, tuple):
        user_data_list = list(user_data)
        define_the_type(user_data_list)
