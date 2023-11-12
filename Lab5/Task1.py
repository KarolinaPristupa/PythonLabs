import numpy as np

print("                      --- ЗАДАНИЕ 1 --- \n")

a = 1.21
b = 0.371

y = np.tan(a + b)**2 - np.sqrt(a + 1.5)*np.sqrt(a + 1.5)**(1/3) + a * b ** 5 - b/np.log(a**2)

print("         Результат вычисления выражения из задания 1.1")
print(f"                    y = {y}")

rows = 12
columns = 3

X = np.ones((rows, columns))
X[:, 1] = np.arange(21, 21+12)
X[:, 2] = np.random.randint(60, 82, size=rows)

Y = np.random.uniform(13.5, 16.6, size=rows)

A = np.linalg.inv(X.T @ X) @ X.T @ Y
print("\n         Результат вычисления выражения из задания 1.2")
print(f"                             X")
print(f"{X}")
print(f"                             Y")
print(f"{Y}")
print(f"                             A")
print(f"        {A}")
print("\n                          Погрешность")
print(np.subtract(Y, X @ A))
