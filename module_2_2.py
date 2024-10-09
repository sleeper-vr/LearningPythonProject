a = input('Введите первое целое число: ')
b = input('Введите второе целое число: ')
c = input('Введите третье целое число: ')
if a == b == c:
    result = 3
elif a == b or b == c or a == c:
    result = 2
else:
    result =  0
print(result)
