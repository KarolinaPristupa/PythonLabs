# Напишите программу, демонстрирующую работу try\except\finally

try:
    number = int(input("Введите какую-то циферку: "))
except (ValueError, SyntaxError, NameError):
    print("/ᐠ - ˕ -マ Ⳋ")
    print("Это не циферка")
    print("ฅ ^•ﻌ• ^ ฅ")
    print("Будем считать, что ты ввел 7")
    number = 7
finally:
    print("Ваша циферка это: ", number)