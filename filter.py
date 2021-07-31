def text_x(bad_words, text):
    result = text.split()
    for i in range(len(bad_words)):
        for j in range(len(result)):
            if result[j] == bad_words[i]:
                result[j] = result[j].replace(result[j], '*' * len(result[j]))
            if result[j][-1] == ',' or result[j][-1] == '.':
                if result[j][:-1] == bad_words[i]:
                    result[j] = result[j].replace(result[j][:-1],
                                                  '*' * (len(result[j]) - 1))

    return ' '.join(result)

text_x(['sad', 'mad', 'bad'], "I'm love sad, because, i'm bad")


# def text_x(bad_words, text):
#     result = text.replace(',', '').split()
#     for i in range(len(bad_words)):
#         for j in range(len(result)):
#             if result[j] == bad_words[i]:
#                 result[j] = "*" * len(result[j])
#     if text.replace(',', '').split(' ') == text.split(', '):
#         # print(', '.join(result))
#         return ', '.join(result)
#     else:
#         # print(' '.join(result))
#         return ' '.join(result)
#
# text_x(['sad', 'mad', 'bad'], "I'm love sad because i'm bad")
