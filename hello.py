def square(a):
    return a*a


arr = []

for x in range(0, 100):
    sqr = square(x)
    if sqr > 100:
        break
    else:
        arr.append(square(x))

print(arr)