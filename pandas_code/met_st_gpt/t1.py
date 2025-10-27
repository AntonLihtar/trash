import matplotlib.pyplot as plt
plt.style.use('ggplot')

x = [1, 2, 3]
y = [10, 20, 15]

plt.plot(x, y)
plt.title("Продажи по кварталам")   # заголовок графика
plt.xlabel("Квартал")               # подпись оси X
plt.ylabel("Продажи, тыс. руб.")    # подпись оси Y
plt.grid(True)                      # сетка для удобства чтения
plt.show()