BAD_WORDS = ['sad', 'mad', 'bad']

def text_x(bad_words, text):
    result = text.split()
    for i in range(len(bad_words)):
        for j in range(len(result)):
            if result[j].lower() == bad_words[i]:
                result[j] = result[j].replace(result[j], '*' * len(result[j]))
            if result[j][:-1].isalpha() == True:
                if result[j][:-1].lower() == bad_words[i]:
                    result[j] = result[j].replace(result[j][:-1],
                                                  '*' * (len(result[j]) - 1))

    return ' '.join(result)

text_x(BAD_WORDS, "Hello Bad")
