import re
from nltk.tokenize import word_tokenize


def longest_even_word(sentence):
    "write your solution here"
    regex = re.compile('\w*\d\w*')
    sentence = regex.sub(' ', sentence)
    words = word_tokenize(sentence.lower())
    even = [(words[i], len(words[i])) for i in range(len(words)) if len(words[i]) % 2 == 0]
    word_1 = [even[i][1] for i in range(len(even))]
    if len(word_1) == 0:
        return 0
    else:
        first_greatest_number_index = word_1.index(max(word_1))
    return even[first_greatest_number_index][0]
