# Создай функцию, которая получает на вход два списка и генерирует график,
#  в качестве ответа: возвращает название файла с графиком.

# График, в котором будет отображаться дневная и ночная температура.
#  По оси X - дни недели, по оси Y - значения температуры.
#  График  дневной температуры красного цвета, ночной - синего.

import matplotlib.pyplot as plt
import random

def temperature_plot(Days, Temp_Days, Temp_Night, File_Name="temperature_plot.png"):
  plt.figure(figsize=(8, 6))
  plt.plot(Days,Temp_Days, marker='o', color='r', linestyle='--', label='Дневная температура')
  plt.plot(Days,Temp_Night, marker='o', color='b', linestyle='--', label='Ночная температура')
  plt.title('Температура по дням недели')
  plt.xlabel('дни недели')
  plt.ylabel('Температура, °C')
  plt.legend()
  plt.savefig(File_Name)
  plt.close()
  return File_Name

Day = [random.randint(10,25) for _ in range(7)]
Nights = [random.randint(7,15) for _ in range(7)]
Weeks = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']

File_Path = temperature_plot(Weeks, Day, Nights)
print(f'Файл сохронить в {File_Path}')



