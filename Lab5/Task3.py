import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

print("---З А Д А Н И Е   3.1---\n")

x = 3.47
del_a = 2

a_values = np.arange(0, 2.01, del_a)

f = np.exp(a_values*x) - 3.45*a_values

for a, f_one in zip(a_values, f):
    print(f"a: {a:.2f}, f(a): {f_one:.2f}")

min_val = np.min(f)
max_val = np.max(f)
mean_val = np.mean(f)

array_size = len(f)
sorted_values = np.sort(f)

print(f"\nМинимальное значение: {min_val:.2f}")
print(f"Максимальное значение: {max_val:.2f}")
print(f"Среднее значение: {mean_val:.2f}")
print(f"Количество элементов: {array_size}")
print(f"Отсортированный массив:{sorted_values}")

plt.plot(a_values, f, label='f(a)')
plt.axhline(y=mean_val, color='r', linestyle='--', label='Среднее значение')
plt.xlabel('a')
plt.ylabel('f(a)')
plt.title('График')
plt.legend()
plt.grid(True)
plt.show()

print("\n---З А Д А Н И Е   3.2---\n")

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

z1 = x**0.25 + y**0.25
z2 = x**2 + y**2
z3 = 2*x + 3*y
z4 = x**2 - y**2
z5 = 2 + 2*x + 2*y - x**2 - y**2

fig = plt.figure(figsize=(15, 10))

ax1 = fig.add_subplot(151, projection='3d')
ax1.plot_surface(x, y, z2, cmap='viridis')
ax1.set_title(r'$z_1 = x^{0.25} + y^{0.25}$')

ax2 = fig.add_subplot(152, projection='3d')
ax2.plot_surface(x, y, z1, cmap='viridis')
ax2.set_title(r'$z_2 = x^{2} + y^{2}$')

ax3 = fig.add_subplot(153, projection='3d')
ax3.plot_surface(x, y, z3, cmap='viridis')
ax3.set_title(r'$z_3 = {2}*x + {3}*y$')

ax4 = fig.add_subplot(154, projection='3d')
ax4.plot_surface(x, y, z4, cmap='viridis')
ax4.set_title(r'$z_4 = {2}*x - {2}*y$')

ax5 = fig.add_subplot(155, projection='3d')
ax5.plot_surface(x, y, z5, cmap='viridis')
ax5.set_title(r'$z_5 = {2} + {2}*x + {2}*y - x^{2} - y^{2}$')

plt.show()
