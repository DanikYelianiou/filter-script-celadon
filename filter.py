bad_words = ['sad', 'mad', 'bad']

# text = "I'm love sad because i'm bad"
text = "sad, mad, bad"


def text_x():
    result = text.replace(',', '').split()
    for i in range(len(bad_words)):
        for j in range(len(result)):
            if result[j] == bad_words[i]:
                result[j] = "*" * len(result[j])
    if text.replace(',', '').split(' ') == text.split(', '):
        print(', '.join(result))
    else:
        print(' '.join(result))

text_x()
