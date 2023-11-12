# Найти в матрице первую строку, все элементы которой упорядочены по возрастанию.
# Изменить упорядоченность элементов этой строки на обратную


import random

def generate_m(n, m):
    matrix = []
    for _ in range(n):
        row = [random.randint(1, 10) for _ in range(m)]
        matrix.append(row)
    return matrix


def print_m(matrix):
    for row in matrix:
        print(row)


def is_sorted(matrix):
    for i, row in enumerate(matrix):
        if all(row[j] <= row[j+1] for j in range(len(row)-1)):
            matrix[i] = reverse_row(row)
            print(f"Упорядоченный по возрастанию столбец номер {i}")
    return matrix


def reverse_row(row):
    return list(reversed(row))


n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
matrix = generate_m(n, m)
print("\n")
print("Ваша матрица была сгенерирована")
print_m(matrix)
matrix = is_sorted(matrix)
print("\n")
print("Измененная матрица")
print_m(matrix)