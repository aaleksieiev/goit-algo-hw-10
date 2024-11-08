import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2 + x ** 3 + x ** 4

def plot(a, b):
    # Створення діапазону значень для x
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування від ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()

def calculate_with_quad(func, a, b):


    # Обчислення інтеграла
    result, error = spi.quad(func, a, b)

    print("Інтеграл: ", result, error)

def calculate_with_monte_carlo(func, a, b, y_min, y_max, num_points):
    x = np.random.uniform(a, b, num_points)
    y = np.random.uniform(y_min, y_max, num_points)
    under_curve = np.sum(y < func(x))
    area = (b - a) * (y_max - y_min) * (under_curve / num_points)
    print("Монте карло: ", area)
    return area
    

a = -1 # нижня межа
b = 1 # верхня межа
y_min = 0
y_max = 5
plot(a, b)
calculate_with_quad(f, a, b)
calculate_with_monte_carlo(f, a, b, y_min, y_max, 1_000_000)
