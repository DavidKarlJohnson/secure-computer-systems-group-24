import os
import random
import math

script_dir = os.path.dirname(os.path.abspath(__file__))
words_path = os.path.join(script_dir, 'wordslist.txt')

def file_to_list(path):
    with open(path, 'r', encoding='utf-8') as fh:
        return fh.read().splitlines()
    

def build_password(nr_words, words_list):
    password = ''
    for i in range (nr_words):
        password += words_list[random.randrange(0, len(words_list) - 1)]
    return password


# a-z, A-Z, 0-9
def calculate_entropy(str):
    return math.log2(62) * len(str)


words_list = file_to_list(words_path)

while True:
    nr_words = int(input('Number of words: '))
    pw = build_password(nr_words, words_list)
    entropy = calculate_entropy(pw)
    print(pw)
    print(f'{nr_words} RANDOM words from word list of {(len(words_list))} words')
    print(f'Entropy: {entropy} bits')
    print(f'You need {entropy / calculate_entropy('a')} RANDOM characters in [a-z, A-Z, 0-9] to get the same entropy.\n')