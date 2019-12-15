import re
from collections import Counter


APOSTROPHE_LIST = {"can't": "can not",
                   "'d": " would",
                   "'ve": " have",
                   "it's": "it is",
                   "doesn't": "does not",
                   "don't": "do not",
                   "'ll": " will",
                   "weren't": "were not",
                   "'re": " are",
                   "wasn't": "was not",
                   "what's": "what is",
                   "who's": "who is",
                   "where's": "where is",
                   "let's": "lets",
                   }


WORD = re.compile(r'\w+')


def apostrophe_cleaner(text):
    for key in APOSTROPHE_LIST.keys():
        text = text.replace(key, APOSTROPHE_LIST[key])
    text = text.replace("'", "")
    return text


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)
