from pwdgenerator import Generator
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


identifier = 'Vasilyev'
N = len(identifier)

passwords = []

# Вариант 1
passwords.append(Generator.generate_by_templates([
    ascii_uppercase,
    ascii_uppercase,
    [(len(identifier) ** 2) % 10],
    digits,
    ['!', "''", '#', '$', '%', '&', "'", '(', ')', '*'],
    ascii_lowercase
]))

# Вариант 2
passwords.append(Generator.generate_by_templates([
    ascii_lowercase,
    ascii_lowercase,
    ascii_lowercase,
    ascii_uppercase,
    ascii_uppercase,
    [N ** 4 % 100],
    [N ** 4 % 100]
]))

# Вариант 3
passwords.append(Generator.generate_by_templates([
    *[digits] * 3,
    ['!', "''", '#', '$', '%', '&', "'", '(', ')', '*'],
    ['!', "''", '#', '$', '%', '&', "'", '(', ')', '*'],
    ascii_uppercase, # Не указан в таблице
    ascii_uppercase,
    [ascii_lowercase[N ** 2 % 10 + N ** 3 % 10 + 1]]
]))

# Вариант 4
passwords.append(Generator.generate_by_templates([]))

# Вариант 5
passwords.append(Generator.generate_by_templates([
    *[digits] * 3,
    ['!', "''", '#', '$', '%', '&', "'", '(', ')', '*'],
    ['!', "''", '#', '$', '%', '&', "'", '(', ')', '*'],
    ascii_uppercase,
    ascii_uppercase,
    [ascii_lowercase[N ** 2 % 10 + N ** 3 % 10 + 1]]
]))

print(passwords)