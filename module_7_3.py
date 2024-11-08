class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    chars = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for char in chars:
                        line = line.replace(char, ' ')
                    line = line.split()
                    words.extend(line)
                    all_words.update({file.name:words})
        return all_words


    def find(self, word):
        for i in range(len(self.file_names)):
            number = {}
            for name, words in self.get_all_words().items():
                if word.lower() in words:
                    n = words.index(word.lower()) + 1
                number.update({name:n})
        return number


    def count(self, word):
        for i in range(len(self.file_names)):
            counter = {}
            for name, words in self.get_all_words().items():
                c = 0
                for i in range(len(words)):
                    if word.lower() == words[i]:
                        c += 1
                counter.update({name:c})
        return counter


finder2 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('tHe')) # 3 слово по счёту
print(finder2.count('thE')) # 4 слова teXT в тексте всего
