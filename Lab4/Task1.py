# Класс Example. В нём пропишите 3 (метода) функции.
# Две переменные задайте статически, две динамически.
# Первый метод: создайте переменную и выведите её.
# Второй метод: верните сумму 2-ух глобальных переменных.
# Третий метод: верните результат возведения первой динамической переменной во вторую динамическую переменную.
# Создайте объект класса. Напечатайте оба метода. Напечатайте переменную a.

class Example:
    static_var_1 = 8
    static_var_2 = 20

    def __init__(self, dynamic_var_1, dynamic_var_2):
        self.dynamic_var_1 = dynamic_var_1
        self.dynamic_var_2 = dynamic_var_2

    def create_and_print(self):
        self.dynamic_var_1 = int(input("Введите значение: "))
        self.dynamic_var_2 = int(input("Введите значение: "))
        element: Example = Example(self.dynamic_var_1, self.dynamic_var_2)
        print(f"Теперь значение переменных dynamic_var_1: {self.dynamic_var_1} и dynamic_var_2: {self.dynamic_var_2}")
        return element

    @staticmethod
    def return_sum():
        return Example.static_var_1 + Example.static_var_2

    def return_method_three(self):
        return self.dynamic_var_1 ** self.dynamic_var_2


obj = Example(0, 0)
obj.create_and_print()

print(f"Сумма {obj.static_var_1} и {obj.static_var_2}: {obj.return_sum()}")
print(f"Возведение {obj.dynamic_var_1} в степень {obj.dynamic_var_2}: {obj.return_method_three()}")
