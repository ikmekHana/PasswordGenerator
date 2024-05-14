from random import choice

illegible_characters = 'il1Io0O'
digits = '23456789'
lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

print('Welcome to the password generator!')
print('Here you can generate the required number of passwords')
print('by selecting their length and characters for generation')

def number_introduction():
    while True:
        number = input()
        if number.isdigit() is True:
            return int(number)
        else:
            print('Enter the correct value - number')

def answer_introduction():
    while True:
        print('Enter "y" if yes or "n" if no')
        answer = input()
        if answer == 'y' or answer == 'Y':
            return True
        elif answer == 'n' or answer == 'N':
            return False
        else:
            print('Please enter the correct value')

def password_generator(password_length, chars):
    password = ''
    for _ in range(password_length):
        password += choice(chars)
    print(password)

while True:
    chars = ''
    print('Enter a number - the required number of passwords')
    number_of_passwords = number_introduction()
    print('Enter a number - the length of one password')
    password_length = number_introduction()
    print('Should I include unintelligible characters in the password?')
    print(f'({illegible_characters})')
    if answer_introduction() is True:
        chars += illegible_characters
    print('Should I include numbers in the password?')
    print(f'({digits})')
    if answer_introduction() is True:
        chars += digits
    print('Should I include lowercase letters in the password?')
    print(f'({lowercase_letters})')
    if answer_introduction() is True:
        chars += lowercase_letters
    print('Should I include uppercase letters in the password?')
    print(f'({uppercase_letters})')
    if answer_introduction() is True:
        chars += uppercase_letters
    print('Should I include characters in the password?')
    print(f'({punctuation})')
    if answer_introduction() is True:
        chars += punctuation
    for i in range(1, number_of_passwords + 1):
        print(f'{i})', end=' ')
        password_generator(password_length, chars)

    print('Want to generate new passwords?')
    if answer_introduction() is False:
        break

print('Thanks for using the password generator!')
print('See you soon!')