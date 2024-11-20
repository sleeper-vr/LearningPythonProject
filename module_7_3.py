

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        words = {}
        symbols_to_remove = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                file_text = file.read()
                words[file_name] = [word.lower().strip(str(symbols_to_remove)) for word in file_text.split()]
        return words

    def find(self, word):
        result = {}
        words = self.get_all_words()
        for file_name, file_words in words.items():
            if word.lower() in file_words:
                result[file_name] = file_words.index(word.lower()) + 1
        return result

    def count(self, word):
        result = {}
        words = self.get_all_words()
        for file_name, file_words in words.items():
            result[file_name] = file_words.count(word.lower())
        return result


finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))

finder1 = WordsFinder('Rudyard Kipling - If.txt',)

print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')

print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))
