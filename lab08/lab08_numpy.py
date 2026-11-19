import numpy as np

hours = np.arange(0, 24, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("Задание 1")
print("hours:", hours)
print("shape:", hours.shape, "ndim:", hours.ndim,
      "size:", hours.size, "dtype:", hours.dtype)
print("line:", line)
print("zeros:", zeros, "dtype:")
print("unknown_table:\n", unknown_table)
print("identity:\n", identity)

print("Задание 2")
print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Индексы 2–5:", hours[2:6])
print("Каждый второй:", hours[::2])
print("В обратном порядке:", hours[::-1])

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("Задание 3")
print("форма:", temperatures.shape,
      "кол-во измерений:", temperatures.ndim,
      "размер:", temperatures.size)
print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:\n",
      temperatures[:2, 1:])
print("Центральный фрагмент 2×2:\n", temperatures[0:2, 1:3])
print("Его форма:", temperatures[0:2, 1:3].shape)

matrix = np.arange(1, 26).reshape(5, 5)

print("Задание 4")
print("matrix:\n", matrix)

top3 = matrix[:3]
print("\nПервые три строки:\n", top3, "\nshape:", top3.shape)

last2 = matrix[-2:]
print("\nПоследние две строки:\n", last2, "\nshape:", last2.shape)

first2cols = matrix[:, :2]
print("\nПервые два столбца:\n", first2cols, "\nshape:", first2cols.shape)

block = matrix[1:4, 2:5]
print("\nСтроки 1–3, столбцы 2–4:\n", block, "\nshape:", block.shape)

corner = matrix[-2:, -2:]
print("\nПравый нижний блок 2×2:\n", corner, "\nshape:", corner.shape)

print("Задание 5")

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
print("vector после vector[1:4] = 0:", vector)

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
print("small_matrix:\n", small_matrix)

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1
print("\nchanged_hours:", changed_hours)
print("исходный hours:", hours)

#.copy нужен для создания копии. Без этого создается ссылка на уже существующий объект, а не новый

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100
print("\nchanged_matrix:\n", changed_matrix)
print("исходная matrix:\n", matrix)

print("Задание 6")
numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T
print("numbers shape:", numbers.shape)
print("table shape:", table.shape)
print("transposed shape:", transposed.shape)

# reshape(3, 4) работает, потому что 3 * 4 = 12 совпадает с size(numbers) = 12:
# reshape сохраняет общее число элементов. reshape(5, 3) вызовет ошибку,
# так как 5 * 3 = 15 ≠ 12 — число элементов изменилось бы, а это запрещено
