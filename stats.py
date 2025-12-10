import os

def count_words(text):
    data = text.split()
    return (f'Found {len(data)} total words')

def count_chars(text):
    temp_dict = {}
    for i in text:
        temp_dict[i] = temp_dict.get(i, 0) +1
    return temp_dict

def sort_dict(dictionary):
    for key, value in (sorted(dictionary.items(), key = lambda x: x[1], reverse= True)):
        yield(key, value)
