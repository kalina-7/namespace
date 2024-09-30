def single_root_words(*other_words, root_word = 'rich'):
    same_words = []
    for i in other_words:
        if root_word in i and i != root_word:
            same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')


def single_root_words(*other_words, root_word = 'Disable'):
    same_words = []
    for i in other_words:
        if i.lower() in root_word.lower():
            same_words.append(i)
    return same_words


result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
