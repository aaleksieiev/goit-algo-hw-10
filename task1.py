import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Product Manufacturing", pulp.LpMaximize)

# Визначення змінних
X1 = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')  # Кількість лимонаду
X2 = pulp.LpVariable('Juice', lowBound=0, cat='Integer')  # Кількість фруктового соку

# Функція цілі (Максимізація кількості виробленої продукції)
model += X1 + X2, "Product quantity"

# Додавання обмежень
model += 2 * X1 + 1 * X2 <= 100  # Обмеження на воду
model += 1 * X1 + 0 * X2 <= 50  # Обмеження на цукор
model += 1 * X1 + 0 * X2 <= 30  # Обмеження на лимоний сік
model += 0 * X1 + 2 * X2 <= 40  # Обмеження на фруктове пюре

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Виробляти лимонад:", X1.varValue)
print("Виробляти фруктовий сік:", X2.varValue)
