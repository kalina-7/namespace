def print_params(a = 5, b = 'moon', c = True):
    print(a, b, c)


print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [5, False, 'питон']
print_params(*values_list)

values_dict = {'a': 5.5, 'b': 'laptop', 'c': 7}
print_params(**values_dict)

values_list_2 = ['sunday', 7.62]
print_params(*values_list_2, 42)


def append_to_list(item, list_my=None):
    if list_my is None:
        list_my = []
    list_my.append(item)
    print(list_my)


append_to_list(45)
