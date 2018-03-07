import random

k = random.uniform(-5, 5)
c = random.uniform(-5, 5)

# Вывод данных начальной прямой
print('Начальная прямая: ', k, '* X + ', c)

# Набор точек X:Y
data = {
    1: 2,
    2: 4.2,
    2.5: 5,
    3.8: 7.9,
    4: 9,
    6: 10.2,
    6.6: 13,
    7.2: 15.3,
    8: 17.1,
    8.5: 19.5
}

# Скорость обучения
rate = 0.0001

def proceed(x):
    return k*x +c

for i in range(100000):
    # random x
    x = random.choice(list(data.keys()))

    correct_result = data[x]

    calc_result = proceed(x)

    delta = correct_result - calc_result

    k += delta*x*rate

    c += delta*rate

# Вывод данных готовой прямой
print('Готовая прямая: ', k, '* X + ', c)


