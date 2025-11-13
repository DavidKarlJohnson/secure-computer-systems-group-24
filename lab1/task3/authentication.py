import os
import random

script_dir = os.path.dirname(os.path.abspath(__file__))
words_path = os.path.join(script_dir, 'wordslist.txt')


def file_to_list(path):
    with open(path, 'r', encoding='utf-8') as fh:
        return fh.read().splitlines()
    

def build_password(nr_words, words_list):
    password = ''
    for i in range (nr_words):
        password += " " + words_list[random.randrange(0, len(words_list))]
    return password



words_list = file_to_list(words_path)

print(build_password(2, words_list))


