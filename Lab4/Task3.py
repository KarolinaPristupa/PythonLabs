# Создать классы «Зоомагазин», «Животное», «Рыбы», «Птицы».
# Определить свойства: породу и стоимость для указанных животных (рыб, птиц),
# в каждом классе реализовать переопределение метода «способ передвижения».
# Вывести данные о самой дорогой породе. Предусмотреть метод записи информации в файл.

class Animal:
    def __init__(self, breed, cost):
        self.breed = breed
        self.cost = cost

    @staticmethod
    def enter_data(self):
        breed = input("Введите породу: ")
        cost = float(input("Введите стоимость: "))
        return Animal(breed, cost)

    def write_to_file(self):
         with open("Animals_store.txt", "a", encoding="utf-8") as store:
             data = self.enter_data()
             store.write(f"Порода: {data.breed}, Стоимость: {data.cost}\n")

class Fish(Animal):
    def mode_of_transporting(self):
        print("Рыбка плавает")


class Bird(Animal):
    def mode_of_transporting(self):
        print("Птичка летает")


class Pet_store:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def find_expensive(self):
        if not self.animals:
            print("В магазине пока что нет животных. Зайдите позже")
            return

        most_exp_animal = max(self.animals, key = lambda animal: animal.cost)
        print(f"Самая дорогая порода: {most_exp_animal.breed} eе цена: {most_exp_animal.cost}")

    def read_from_file(self):
        with open("Animals_store.txt", "r", encoding="utf-8") as store:
            for line in store:
                parts = line.split(", ")
                breed = parts[0].replace("Порода: ", "")
                cost = float(parts[1].replace("Стоимость: ", ""))
                animal = Animal(breed, cost)
                self.animals.append(animal)
            animals = store.readlines()


pet_store = Pet_store()
while(1):
    choice = int(input("       МЕНЮ      \n1.Добавить животное\n2.Вывести самую дорогую породу\n3.Выйти\n     Ответ: "))
    if choice == 1:
        type = int(input("1.Рыбы\n2.Птицы\n     Ответ: "))
        if type == 1:
            animal = Fish(" ", 0)
            animal.write_to_file()
            pet_store.add_animal(animal)
        elif type == 2:
            animal = Bird(" ", 0)
            animal.write_to_file()
            pet_store.add_animal(animal)
        else:
            print("Неправильный тип животного")




    elif choice == 2:
        pet_store.read_from_file()
        pet_store.find_expensive()
    elif choice == 3:
        break

