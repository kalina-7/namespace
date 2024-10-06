data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data):
    counts = 0

    def flatten(data):
        nonlocal counts

        if isinstance(data, list) or isinstance(data, tuple) or isinstance(data, set):
            for item in data:
                flatten(item)
        elif isinstance(data, dict):
            for key in data.keys():
                flatten(key)
            for value in data.values():
                flatten(value)
        else:
            if isinstance(data, int):
                counts += data
            else:
                counts += len(data)

    flatten(data)

    return counts


result = calculate_structure_sum(data_structure)
print(result)
