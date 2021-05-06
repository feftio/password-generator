from pwdgenerator import Vigenere
from rich.console import Console
from rich.table import Table

ENGLISH = 'abcdefghijklmnopqrstuvwxyz'
RUSSIAN = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

console = Console()

alphabets = {
    'Русский': 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
    'Русский (без ё)': 'абвгдежзийклмнопрстуфхцчшщъыьэюя',
    'Английский': 'abcdefghijklmnopqrstuvwxyz',
    'Свой собственный': ''
}

def choose_alphabet():
    console.print('Выберите алфавит: ')
    alphabets_keys = list(alphabets.keys())
    alphabets_values = list(alphabets.values())
    for i in range(len(alphabets_keys)):
        console.print(f'{i + 1}. {alphabets_keys[i]}')
    index = abs(int(console.input()))
    console.print(f'Выбран [magenta]{alphabets_keys[index - 1].lower()}[/magenta] алфавит.')
    if len(alphabets_keys) == index:
        return console.input('Введите алфавит: ')
    return alphabets_values[index - 1]

def main(alphabet):
    vigenere = Vigenere(alphabet)
    text = console.input('Введите текст: ')
    key = console.input('Введите ключ: ')
    console.print(f'Расшифрованное значение: [magenta]{vigenere.decrypt(text, key)}[/magenta]')
    console.print(f'Зашифрованное значение: [magenta]{vigenere.encrypt(text, key)}[/magenta]')


if __name__ == '__main__':
    while(True):
        try:
            alphabet = choose_alphabet()
            break
        except:
            console.print('[magenta]Такого индекса нет.[/magenta]')
    while(True):
        main(alphabet)
