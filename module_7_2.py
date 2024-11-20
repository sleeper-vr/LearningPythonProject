

def custom_write(file_name, strings):
    result = {}
    i = 0
    with open(file_name, 'w', encoding='utf-8') as file:
        for string in strings:
            i += 1
            result[(i, file.tell())] = string
            file.write(string + '\n')
    return result



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]


result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
