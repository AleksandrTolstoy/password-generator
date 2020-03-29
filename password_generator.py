import requests
from os.path import isfile
from random import choice, randint

from passwordmeter import test

if not isfile('words.txt'):
    print('Downloading words ...')
    url = r'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
    response = requests.get(url)
    with open('words.txt', 'w') as file:
        file.write(response.text)

words = open('words.txt').read().split('\n')

special_chars = ['.', ',', ':', ';', '?', '!',
                 '*', '+', '%', '-', '<', '>',
                 '@', '[', ']', '{', '}', '/',
                 '\\', '_', '{}', '$', '#']

def create_password(num_words: int = 2, num_numbers: int = 3, num_special: int = 1) -> str:
    pass_str = ''
    for _ in range(num_words):
        pass_str += choice(words).lower().capitalize()
    for _ in range(num_numbers):
        pass_str += str(randint(0, 9))
    for _ in range(num_special):
        pass_str += choice(special_chars)
    return pass_str

def main() -> None:
    pass_str = create_password()
    strength, _ = test(pass_str)
    print(f'Password: {pass_str}\n'
          f'Strength: {strength}')

if __name__ == '__main__':
    main()
