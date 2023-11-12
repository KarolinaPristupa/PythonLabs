# Создать класс Employee (сотрудник) с полями
# ФИО, стаж, часовая заработная плата, количество отработанных часов, оклад, премия.
# Создать список сотрудников компании.
# Реализовать ввод данных всех сотрудников с клавиатуры.
# Рассчитать с помощью методов класса заработную плату за отработанное время, и премию,
# размер которой определяется в зависимости от стажа работника
# (при стаже до 1 года 1%, до 3 лет 5%, до 5 лет 8%, свыше 5 лет 15%).
# С помощью метода печати, реализовать вывод информации о работнике на экран.

class Employee:
    def __init__(self, full_name, experience, hourly_salary_1, hours_work_1, base_salary_1, bonus_rate):
        self.full_name = full_name
        self.experience = experience
        self.hourly_salary = hourly_salary_1
        self.hours_work = hours_work_1
        self.base_salary = base_salary_1
        self.bonus_rate = bonus_rate

    def calculate_salary(self):
        base_payment = self.hourly_salary * self.hours_work
        bonus = 0
        if self.experience < 0:
            bonus = base_payment * 0.01
        elif self.experience < 3:
            bonus = base_payment * 0.05
        elif self.experience < 5:
            bonus = base_payment * 0.08
        elif self.experience >= 5:
            bonus = base_payment * 0.15

        return base_payment + bonus

    def print_information(self):
        print(f"ФИО: {self.full_name}")
        print(f"Опыт: {self.experience}")
        print(f"Зарплата за 1 час: {self.hourly_salary}")
        print(f"Количество часов работы: {self.hours_work}")
        print(f"Оклад: {self.base_salary}")
        print(f"Премия: {self.calculate_salary() - (self.hourly_salary * self.hours_work)}")
        print(f"Зарплата: {self.calculate_salary()}\n")


employees = []


number = int(input("Введите количество: "))
for _ in range(number):
    name = input("Введите ФИО сотрудника: ")
    exp = float(input("Введите стаж сотрудника (в годах): "))
    hourly_salary = float(input("Введите часовую заработную плату: "))
    hours_work = int(input("Введите часы работы: "))
    base_salary = float(input("Введите оклад сотрудника: "))
    employee = Employee(name, exp, hourly_salary, hours_work, base_salary, 0)
    employees.append(employee)

for employee in employees:
    employee.print_information()
