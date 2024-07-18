import matplotlib.pyplot as plt
import random

random_numbers = [random.randint(1, 100) for _ in range(10)]

plt.figure(figsize=(8, 6))
plt.plot(range(1, 11), random_numbers, marker='o', color='r', linestyle='--')
plt.title('График случайных чисел')
plt.xlabel('Индекс')
plt.ylabel('Значение')
plt.grid(True)
plt.show()


# Создаем список из 10 случайных чисел.
# Каждое число в этом списке находится в диапазоне от 1 до 100. 
# Здесь используется метод randint из модуля random, который выбирает случайное число в указанном диапазоне. 
# Конструкция for _ in range(10) повторяет этот процесс 10 раз, чтобы получить 10 чисел.
random_numbers = [random.randint(1, 100) for _ in range(10)]

# Настройка размера фигуры графика (ширина 8 дюймов, высота 6 дюймов)
plt.figure(figsize=(8, 6))

# Создание линейного графика: по оси X идут числа от 1 до 10, по оси Y - случайные числа
# marker='o' означает, что каждое значение будет отмечено круглым маркером
# color='r' задает красный цвет линии
# linestyle='--' задает стиль линии (пунктирная)
plt.plot(range(1, 11), random_numbers, marker='o', color='r', linestyle='--')

# Задаем заголовок графика
plt.title('График случайных чисел')

# Задаем название оси X
plt.xlabel('Индекс')

# Задаем название оси Y
plt.ylabel('Значение')

# Включаем сетку на графике для удобства восприятия данных
plt.grid(True)

plt.savefig("Numbers.jpg")

# Отображаем график
plt.show()
