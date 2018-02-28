import random;

numbers = [
    list('111101101101111'),
    list('001001001001001'),
    list('111001111100111'),
    list('111001111001111'),
    list('101101111001001'),
    list('111100111001111'),
    list('111100111101111'),
    list('111001001001001'),
    list('111101111101111'),
    list('111101111001111')
]

numbers5 = [
    list('111100111000111'),
    list('111100010001111'),
    list('111100011001111'),
    list('110100111001111'),
    list('110100111001011'),
    list('111100101001111')
]

# Инициализация весов сети
weights = [0 for i in range(15)]

# Порог функции активации
bias = 9

def proceed(number):
    net = 0
    for i in range(0, 15):
        net += int(number[i])*weights[i]

    return net >= bias

# Уменьшение значений весов, если сеть ошиблась и выдала 1
def decreaseWeight(number):
    for i in range(0, 15):
        # Если вход возбужден - уменьшаем вес
        if int(number[i]) == 1:
            weights[i] -= 1

# Увеличение значений весов, если сеть ошиблась и выдала 0
def increaseWeight(number):
    for i in range(0, 15):
        # Если вход возбужден - увеличивааем вес
        if int(number[i]) == 1:
            weights[i] += 1


for j in range(0, 10000):
    testValue = random.randint(0, 9)

    if testValue != 5:
        # Если сеть выдала True/Да/1, то наказываем ее
        if proceed(numbers[testValue]) == 1:
            decreaseWeight(numbers[testValue])
    else:
        # Если сеть выдала False/Нет/0, то показываем, что эта цифра - то, что нам нужно
        if not proceed(numbers[5]):
            increaseWeight(numbers[5])

# Вывод значений весов
print(weights)

# Прогон по обучающей выборке
for t in range(0, 9):
    print(t, " это 5?", proceed(numbers[t]))

# Прогон по тестовой выборке
print("Узнал 5? ", proceed(numbers[5]))
for m in range(0, len(numbers5)):
    print("Узнал 5 - ", m, "? ", proceed(numbers5[m]))

