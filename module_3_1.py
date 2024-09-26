calls = 0

def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return  len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = map(str.lower, list_to_search)
    if string in list_to_search:
        return True
    else:
        return False


print(string_info('Table'))
print(string_info('Drummer'))
print(is_contains('MoDulE', ['good', 'table', 'Life', 'mOdUle'])) # MoDulE ~ mOdUle
print(is_contains('Canberra', ['moon', 'position', 'Post', 'appointment'])) # No matches
print(calls)
