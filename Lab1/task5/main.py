import locale
import datetime

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
print("---ЮВЕЛИРНЫЙ МАГАЗИН---")

information = {
    "Серьги  6354DE": ["Серебро", 3824.99, 3],
    "Серьги  76RT90": ["Золото ", 1588.25, 4],
    "Серьги  982T9S": ["Серебро", 68.64, 10],
    "Кольцо  766SA5": ["Серебро", 2291.79, 5],
    "Колье   U9I787": ["Золото ", 112.99, 8],
    "Колье   A09J8A": ["Серебро", 270.18, 3],
    "Колье   K765H4": ["Золото ", 54.87, 5],
    "Браслет OP333P": ["Серебро", 1361.25, 7],
    "Браслет JJJ783": ["Серебро", 187.44, 8]
}

purchases = []

def View_descriptions():
    print("   Название         Материал")
    for i in information:
        description = information[i][0]
        print(f"{i}      {description}")


def View_prices():
    print("   Название        Стоимость")
    for i in information:
        price = information[i][1]
        print(f"{i}      {price}")


def View_amounts():
    print("   Название        Количество ")
    for i in information:
        amount = information[i][2]
        print(f"{i}         {amount}")


def View_all():
    print("   Название         Материал    Стоимость    Количество ")
    for i in information:
        description = information[i][0]
        price = information[i][1]
        amount = information[i][2]
        if price < 100:
            print(f"{i}      {description}      {price}           {amount}")
        elif price < 1000:
            print(f"{i}      {description}      {price}          {amount}")
        else:
            print(f"{i}      {description}      {price}         {amount}")


def Make_a_purchase():
    View_all()
    number = int(input("Введите номер изделия: "))
    if number < 1:
        print("Номер не может быть меньше 1!")
    elif number > len(information):
        print("Выход за пределы списка!")
    else:
        key = list(information.keys())[number - 1]
        amount_of_product = information[key][2]
        if amount_of_product == 0:
            print("Товар закончился на складе!")
        else:
            print("Товар найден!")
            amount = int(input("Введите количество: "))
            if amount < 0:
                print("Количество не может быть меньше 1!")
            elif amount > amount_of_product:
                print("Столько товара нет на складе!")
            else:
                information[key][2] -= amount
                total_cost = amount * information[key][1]
                purchases.append((key, amount, total_cost))
                print(f"Сумма покупки: {total_cost} руб.")
                print("Покупка добавлена в чек.")

def make_a_check():
    if not purchases:
        print("Чек пуст.")
        return

    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    total_cost = sum(purchase[2] for purchase in purchases)

    print("    D I A M O N D ")
    print("**********************")
    print("   www.diamond.com")
    print("   8 904 500 77 77")
    print("**********************")
    print("Кассир: Орлова Ж.Д.")
    print(formatted_datetime)
    print("Продажа         №4556")
    print("**********************")

    for purchase in purchases:
        key, amount, cost = purchase
        print(f"{key} * {amount}  ")
        print(f"         {cost} руб.")

    print("**********************")
    print(f"ИТОГО:    {total_cost} руб.")
    print("**********************")
    print(" !СПАСИБО ЗА ПОКУПКУ!")

while True:
    print("\nМеню:")
    print("1. Показать описания")
    print("2. Показать цены")
    print("3. Показать количество")
    print("4. Показать всю информацию")
    print("5. Совершить покупку")
    print("6. Сформировать чек")
    print("0. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        View_descriptions()
    elif choice == "2":
        View_prices()
    elif choice == "3":
        View_amounts()
    elif choice == "4":
        View_all()
    elif choice == "5":
        Make_a_purchase()
    elif choice == "6":
        make_a_check()
    elif choice == "0":
        break
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
