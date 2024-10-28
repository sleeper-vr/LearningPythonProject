def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(5)
print_params(5, 4)
print_params(5, 4, 3)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [4, '123', False,]
values_dict = {'a': 4, 'b': '123', 'c': False,}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [7, '555']
print_params(*values_list_2, 42)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)