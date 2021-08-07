BAD_WORDS = ['sad', 'mad', 'bad']

def text_x(bad_words, text):
    result = text.split()
    for word in enumerate(bad_words):
        for index, list_word in enumerate(result):
            if list_word.lower() == word[1]:
                result[index] = list_word.replace(list_word, '*' * len(list_word))
            elif word[1] in list_word.lower():
                result[index] = list_word.replace(list_word[:-(len(list_word) - len(word[1]))], '*' * len(word[1]))
    return ' '.join(result)

text_x(BAD_WORDS, "Hello Baded!!!!!")
