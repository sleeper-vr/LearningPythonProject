

def calculate_structure_sum(data_structure):
    sum_ = 0

    if isinstance(data_structure, int) or isinstance(data_structure, float):
        sum_ += data_structure
        return sum_
    if isinstance(data_structure, str):
        sum_ += len(data_structure)
        return sum_

    for data in data_structure:
        if isinstance(data, dict):
            for key in data.keys():
                if key.isdigit():
                    sum_ += key
                else:
                    sum_ += len(key)
            for value in data.values():
                sum_ += calculate_structure_sum(value)
        if isinstance(data, list):
            sum_ += calculate_structure_sum(data)
        if isinstance(data, tuple):
            sum_ += calculate_structure_sum(data)
        if isinstance(data, set):
            sum_ += calculate_structure_sum(data)
        if isinstance(data, int) or isinstance(data, float):
            sum_ += data
        if isinstance(data, str):
            sum_ += len(data)

    return sum_


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)

print(result)