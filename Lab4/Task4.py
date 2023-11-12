# Придумать класс самостоятельно,
# реализовать в нем методы экземпляра класса, статические, методы, методы класса.

class Car:
    def __init__(self, model, color, cost):
        self.model = model
        self.color = color
        self.cost = cost

    @classmethod
    def make_car(cls):
        model = input("Введите марку автомобиля: ")
        color = input("Введите цвет автомобиля: ")
        cost = float(input("Введите цену автомобиля: "))
        return Car(model, color, cost)

    def print_info(self):
        print(f"Модель: {self.model}")
        print(f"Цвет: {self.color}")
        print(f"Цена: {self.cost}\n")

    def increase_cost(self, cost):
        self.cost += cost

    @staticmethod
    def compare_cars(car1, car2):
        if car1.cost > car2.cost:
            print("Первая машина дороже")
        elif car1.cost < car2.cost:
            print("Вторая машина дороже")
        else:
            print("Машины равны по цене")


car = Car("", " ", 0)
cars = []
while(1):
    choice = int(input("    МЕНЮ    \n1.Добавить машину\n2.Вывести все\n3.Сравнить\n4.Поднять цену\n5.Выйти\n  Ответ: "))
    if choice == 1:
        car = Car.make_car()
        cars.append(car)
    elif choice == 3:
        a = int(input("Номер первой машины: "))
        b = int(input("Номер второй машины: "))
        car.compare_cars(cars[a], cars[b])
    elif choice == 2:
        for car1 in cars:
            car1.print_info()
    elif choice == 4:
        a = int(input("Номер машины: ")) - 1
        plus_cost = input("На сколько: ")
        cars[a].increase_cost(plus_cost)
    elif choice == 5:
        break