import numpy as np
from prettytable import PrettyTable

def manual_input(n, m):
    Q = []
    print("Введите значения таблицы Q построчно:")
    for i in range(n):
        row = []
        for j in range(m):
            value = int(input(f"Введите значение для строки {i + 1}, столбца {j + 1}: "))
            row.append(value)
        Q.append(row)
    return Q

def random_input(n, m):
    return np.random.randint(1, 20, size=(n, m))

def default_input(n, m):
    return np.array([
        [6, 7, 8, 10],
        [4, 5, 6, 13],
        [10, 6, 5, 11],
        [8, 9, 7, 9],
        [1, 2, 1, 2],
        [2, 1, 2, 4],
        [3, 3, 2, 2],
        [4, 1, 3, 3]
    ])

# Ввод способа заполнения таблицы
print("Выберите способ заполнения таблицы Q:\n \
      1. Ручной ввод \n \
      2. Случайные значения \n \
      3. Значения по умолчанию")

choice = int(input("Введите номер способа (1/2/3): "))

if choice == 1:
    # Ввод количества проектов (n) и состояний (m)
    n = int(input("Введите количество проектов (n): "))
    m = int(input("Введите количество состояний (m): "))
    Q = manual_input(n, m)
elif choice == 2:
    # Ввод количества проектов (n) и состояний (m)
    n = int(input("Введите количество проектов (n): "))
    m = int(input("Введите количество состояний (m): "))
    Q = random_input(n, m)
elif choice == 3:
    n, m = 8, 4
    Q = default_input(n, m)
else:
    print("Неверный выбор способа заполнения.")
    exit()

# Преобразование списка в массив NumPy
Q = np.array(Q)

# Создание таблицы PrettyTable для Q
table = PrettyTable()
table.field_names = ["Проект"] + [f"Состояние {j + 1}" for j in range(m)]

# Добавление строк в таблицу
for i in range(n):
    table.add_row([i + 1] + list(Q[i]))

# Вывод исходной таблицы Q
print("\nТаблица Q:")
print(table)

# Критерий Вальда
wald_values = []
for i in range(n):
    wald = min(Q[i])
    wald_values.append(wald)

# Создание таблицы PrettyTable для Критерия Вальда
table_w = PrettyTable()
table_w.field_names = ["Проект"] + ["Критерий Вальда"]

# Добавление строк в таблицу table_w
for i in range(n):
    table_w.add_row([i + 1] + [wald_values[i]])

# Вывод таблицы Критерия Вальда
print("\nТаблица Критерия Вальда:")
print(table_w)

# Нахождение проекта с минимальным Критерием Вальда
optimal_project = np.argmax(wald_values) + 1
best_wald_value = max(wald_values)

print(f"Оптимальный проект: Проект {optimal_project} с Критерием Вальда = {best_wald_value}")
