def text_x(bad_words, text):
    result = text.replace(',', '').split()
    for i in range(len(bad_words)):
        for j in range(len(result)):
            if result[j] == bad_words[i]:
                result[j] = "*" * len(result[j])
    if text.replace(',', '').split(' ') == text.split(', '):
        # print(', '.join(result))
        return ', '.join(result)
    else:
        # print(' '.join(result))
        return ' '.join(result)

text_x(['sad', 'mad', 'bad'], "I'm love sad because i'm bad")
