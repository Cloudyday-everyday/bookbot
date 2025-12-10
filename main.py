import os
import sys 
from stats import count_words
from stats import count_chars
from stats import sort_dict


if len(sys.argv) ==2:
    filepath = sys.argv[1]

else:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)




def get_text(filepath = filepath):
    with open(filepath) as f:
        file_content = f.read().lower()
    return file_content

def main():
    text = str(get_text())
    print (text)


def program():
    print (f'''========== BOOKBOT ==========
            Analyzing book found at {filepath}...
            --------- WORD COUNT --------
            {count_words(get_text())}
            --------- CHARACTER COUNT ---
            ''')
    for i,j in (sort_dict(count_chars(get_text()))):
        print(f'{i}: {j}')
    print('======== END =======')

program()