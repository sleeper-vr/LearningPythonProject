n = int(input('Введите число от 3 до 20: '))

result = ''
for i in range(1, n):
    for j in range(i, n):
        if n % (i + j) == 0:
            if i != j:
                result += str(i)
                result += str(j)

print(f'{n} - {result}')
