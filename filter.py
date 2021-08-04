BAD_WORDS = ['sad', 'mad', 'bad']

def text_x(bad_words, text):
    result = text.split()
    for id in enumerate(bad_words):
        for i, index in enumerate(result):
            if index.lower() == id[1]:
                result[i] = index.replace(index, '*' * len(index))
            elif id[1] in index.lower():
                result[i] = index.replace(index[:-(len(index) - len(id[1]))], '*' * len(id[1]))
    return ' '.join(result)

text_x(BAD_WORDS, "Hello Baded!!!!!")
