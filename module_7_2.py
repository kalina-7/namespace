strings_positions = {}

def custom_write(file_name, strings):
    f = open(file_name, 'w', encoding='utf-8')
    for i in strings:
        f.tell()
        t = f.tell()
        f.write(str(i))
        f.write('\n')
        strings_positions.update({(strings.index(i)+1, t):i})
    f.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
