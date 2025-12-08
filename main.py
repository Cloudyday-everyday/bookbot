import os
from stats import count_words

filepath = './books/frankenstein.txt'

def get_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def main(filepath):
    text = str(get_text(filepath))
    print (text)

count_words(get_text(filepath))