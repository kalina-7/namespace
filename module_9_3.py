first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
second_result = (len(first[index1]) == len(second[index2]) for index1 in range(len(first)) for index2 in range(len(second)) if index1 == index2)

print(list(first_result))
print(list(second_result))