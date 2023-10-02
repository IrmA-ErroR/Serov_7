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

def wald_function(Q):
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

    return optimal_project, best_wald_value

def savage_function(Q):
    # Находим максимумы для каждого столбца исходной матрицы Q
    max_values = np.max(Q, axis=0)

    # Создаем таблицу PrettyTable для максимумов столбцов
    table_max_values = PrettyTable()
    table_max_values.field_names = [f"Состояние {i + 1}" for i in range(len(max_values))]
    table_max_values.add_row(max_values)

    print("\nМаксимумы для каждого состояния:")
    print(table_max_values)

    # Создаем матрицу рисков
    risk_matrix = max_values - Q

    # Создаем таблицу PrettyTable для матрицы рисков
    table_risk_matrix = PrettyTable()
    table_risk_matrix.field_names = ["Проект"] + [f"Состояние {j + 1}" for j in range(Q.shape[1])]

    # Добавляем строки в таблицу матрицы рисков
    for i in range(risk_matrix.shape[0]):
        table_risk_matrix.add_row([i + 1] + list(risk_matrix[i]))

    print("\nМатрица рисков:")
    print(table_risk_matrix)

    # Находим максимумы для каждой строки матрицы рисков
    max_values_rows = np.max(risk_matrix, axis=1)

    # Создаем таблицу PrettyTable для максимумов строк
    table_max_values_rows = PrettyTable()
    table_max_values_rows.field_names = ["Проект"] + ["Максимум строки"]

    # Добавляем строки в таблицу максимумов строк
    for i in range(len(max_values_rows)):
        table_max_values_rows.add_row([i + 1, max_values_rows[i]])

    print("\nМаксимумы для каждой строки матрицы рисков:")
    print(table_max_values_rows)

    # Находим минимальное значение максимума для строки
    min_max_row = np.min(max_values_rows)

    # Находим индекс строки с минимальным значением максимума
    optimal_project = np.argmin(max_values_rows) + 1
    return optimal_project, min_max_row

def gurwitz_function(Q, alpha=0.6):
    
    min_values = np.min(Q, axis=1)
    max_values = np.max(Q, axis=1)

    # Рассчитываем среднее взвешенное значение для каждой строки
    c_values = alpha * min_values + (1 - alpha) * max_values

    # Создаем таблицу PrettyTable
    table_gurwitz = PrettyTable()
    table_gurwitz.field_names = ["Проект", "min", "max", "с"]

    # Добавляем строки в таблицу
    for i in range(n):
        table_gurwitz.add_row([i + 1, min_values[i], max_values[i], c_values[i]])

    print("\nСтолбцы: проект, min, max, с")
    print(table_gurwitz)

    max_c = np.max(c_values)

    # Находим индекс строки с максималььным значением среднего взвешенного 
    optimal_project = np.argmax(c_values) 

    return optimal_project + 1, max_c

def laplas_function(Q):
    laplas_values = []
    for i in range(n):
        laplas = sum(Q[i]) / m
        laplas_values.append(laplas)

    # Создание таблицы PrettyTable для Критерия Лапласа
    table_l = PrettyTable()
    table_l.field_names = ["Проект"] + ["Критерий Лапласа"]

    # Добавление строк в таблицу table_l
    for i in range(n):
        table_l.add_row([i + 1] + [laplas_values[i]])

    # Вывод таблицы Критерия Лапласа
    print("\nТаблица Критерия Лапласа:")
    print(table_l)

    max_l = np.max(laplas_values)

    # Находим индекс строки с максималььным значением среднего взвешенного 
    optimal_project = np.argmax(laplas_values) 

    return optimal_project + 1, max_l

def bayes_function(Q, vector=[0.1, 0.4, 0.4, 0.1]):
    # Рассчитываем сумму для каждой строки с учетом весовых коэффициентов
    bayes_values = np.dot(Q, vector)

    # Находим максимум из значений критерия Байеса
    max_bayes_value = np.max(bayes_values)

    # Находим индекс строки с максимальным значением критерия Байеса
    optimal_project = np.argmax(bayes_values) + 1

    # Создаем таблицу PrettyTable
    table_b = PrettyTable()
    table_b.field_names = ["Проект"] + ["Критерий Байеса"]

    # Добавляем строки в таблицу
    for i in range(Q.shape[0]):
        table_b.add_row([i + 1] + [bayes_values[i]])
    
    print("\nТаблица Критерия Байеса:")
    print(table_b)

    return optimal_project, max_bayes_value


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
voice_w , value_w = wald_function(Q)
print(f"Оптимальный проект: Проект {voice_w} с Критерием Вальда = {value_w}")

print("\n\nТаблица Q:")
print(table)
voice_s, value_s = savage_function(Q)
print(f"Оптимальный проект: Проект {voice_s} с Критерием Сэвиджа = {value_s}")

print("\n\nТаблица Q:")
print(table)
# a = float(input('\nВведите весовой коэффициент: '))
voice_g, value_g = gurwitz_function(Q) #, a)
print(f"Оптимальный проект: Проект {voice_g} с Критерием Гурвица = {round(value_g, 2)}")

print("\n\nТаблица Q:")
print(table)
voice_l, value_l = laplas_function(Q)
print(f"Оптимальный проект: Проект {voice_l} с Критерием Лапласа = {value_l}")

print("\n\nТаблица Q:")
print(table)
# v = [float(input('\nВведите весовой коэффициент: ')) for _ in range(m)]
voice_b, value_b = bayes_function(Q) #, v)
print(f"Оптимальный проект: Проект {voice_l} с Критерием Байеса = {voice_l}")


# Создание таблицы PrettyTable для Q
table = PrettyTable()
table.field_names = ["Критерий"] + ["Голос"]


# Добавление строк в таблицу
table.add_row(["Критерий Вальда"] + [voice_w])
table.add_row(["Критерий Сэвиджа"] + [voice_s])
table.add_row(["Критерий Гурвица"] + [voice_g])
table.add_row(["Критерий Лапласа"] + [voice_l])
table.add_row(["Критерий Байеса"] + [voice_b])

# Создаем словарь для хранения голосов критериев



criteria_votes = {
    "Критерий Вальда": voice_w,
    "Критерий Сэвиджа": voice_s,
    "Критерий Гурвица": voice_g,
    "Критерий Лапласа": voice_l,
    "Критерий Байеса": voice_b
}

# Создаем векторы голосов
vectors = {criterion: [] for criterion in criteria_votes}

# Заполняем векторы голосов
for criterion, votes in criteria_votes.items():
    vector = [1 if i + 1 == votes else 0 for i in range(n)]
    vectors[criterion] = vector

# Преобразуем векторы голосов в матрицу
voting_matrix = np.array([vectors[criterion] for criterion in criteria_votes])

# Транспонируем матрицу
voting_matrix_transposed = voting_matrix.T


print("\n\nМатрица голосования:")
# Создаем таблицу PrettyTable
voting_table = PrettyTable()
voting_table.field_names = ["Номер проекта"] + list(criteria_votes.keys()) + ["Сумма голосов"]

# Выводим транспонированную матрицу голосов
for i, row in enumerate(voting_matrix_transposed):
    project_name = f"x_{i+1}"
    row_str = [project_name] + list(map(str, row)) + [sum(row)]
    voting_table.add_row(row_str)

# Выводим таблицу
print(voting_table)

# Находим номер проекта с максимальной суммой голосов
max_sum_project = voting_matrix_transposed.sum(axis=1).argmax() + 1
max_sum = max(voting_matrix_transposed.sum(axis=1))

# Выводим номер проекта и сумму голосов
print(f"Проект с максимальной суммой голосов: x_{max_sum_project} (Сумма голосов: {max_sum})")

