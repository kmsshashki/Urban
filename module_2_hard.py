while True:
    n = int(input('Введите число от 3 до 20: '))
    if 2 < n < 21:
        break
result = ''
for i in range(1, n - 1):
    for j in range(i + 1, n):
        if n % (i + j) == 0:
            result += str(i) + str(j)
print(result)
