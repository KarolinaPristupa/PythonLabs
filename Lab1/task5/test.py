def double(x):
    return x * 2

numbers = [1, 2, 3]
doubled_numbers = list(map(double, numbers))
print(doubled_numbers)


def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

result = calculate_factorial(3)
print(result)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


def get_statistics(numbers):
    if len(numbers) == 0:
        return (0, 0, 0)
    mean = sum(numbers) / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    return (mean, minimum, maximum)

data = [12, 54, 16, 28, 40]
statistics = get_statistics(data)
print(statistics[0], statistics[1], statistics[2])


a = ('Hello', 'dear', 'friends', '!')

c = ' '.join(a)

print(c)


a = (11, 27, 31, 9, 3, 32, 30)
print(a[1:3], a[5::])
