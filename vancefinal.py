def get_num_of_non_WS_characters(usr_str):
    count = 0
    for i in usr_str:
        if not i.isspace():
            count += 1
    return count


def get_num_of_words(usr_str):
    count = 0
    for i in range(1, len(usr_str)):
        if (usr_str[i].isspace()) and (not usr_str[i - 1].isspace()):
            count += 1

    if not usr_str[len(usr_str) - 1].isspace():
        count += 1
    return count


def fix_capitalization(usr_str):
    last_char = ' '
    string_edit = ''
    count = 0
    if usr_str[0].islower():
        string_edit = string_edit + usr_str[0].upper()
        count += 1
    else:
        string_edit = string_edit + usr_str[0]

    for i in range(1, len(usr_str)):
        if (last_char == '.' or last_char == '!' or last_char == '?') and usr_str[i].islower():
            string_edit = string_edit + usr_str[i].upper()
            count += 1
        else:
            string_edit = string_edit + usr_str[i]
        if not usr_str[i].isspace():
            last_char = usr_str[i]

    return string_edit, count


def replace_punctuation(usr_str, **kwargs):
    string_edit = ''
    for i in usr_str:
        if i == '!':
            string_edit = string_edit + '.'
            kwargs['exclamation_count'] += 1
        elif i == ';':
            string_edit = string_edit + ','
            kwargs['semicolon_count'] += 1
        else:
            string_edit = string_edit + i

    print('Punctuation replaced')
    print(f"exclamation_count: {kwargs['exclamation_count']}")
    print(f"semicolon_count: {kwargs['semicolon_count']}")

    return string_edit


def shorten_space(usr_str):
    string_edit = ''
    for i in range(1, len(usr_str)):
        if not (usr_str[i].isspace() and usr_str[i - 1].isspace()):
            string_edit = string_edit + usr_str[i - 1]
        if i == (len(usr_str) - 1):
            string_edit = string_edit + usr_str[i]

    return string_edit


def print_menu():
    print('MENU')
    print('c - Number of non-whitespace characters')
    print('w - Number of words')
    print('f - Fix capitalization')
    print('r - Replace punctuation')
    print('s - Shorten spaces')
    print('e - Encrypt text')
    print('d - Decrypt text')
    print('y - Count occurrences of a specific word')
    print('q - Quit\n')


def execute_menu(option, usr_str):
    if option == 'c':
        print(f'Number of non-whitespace characters: {get_num_of_non_WS_characters(usr_str)}\n')
    elif option == 'w':
        print(f'Number of words: {get_num_of_words(usr_str)}\n')
    elif option == 'f':
        new_str, capital_count = fix_capitalization(usr_str)
        print(f'Number of letters capitalized: {capital_count}')
        print(f'Edited text: {new_str}\n')
    elif option == 'r':
        new_str = replace_punctuation(usr_str, exclamation_count=0, semicolon_count=0)
        print(f'Edited text: {new_str}\n')
    elif option == 's':
        new_str = shorten_space(usr_str)
        print(f'Edited text: {new_str}\n')
    elif option == 'e':
        shift = int(input('Enter the shift value for encryption: '))
        encrypted_text = caesar_cipher(usr_str, shift)
        print(f'Encrypted text: {encrypted_text}\n')
    elif option == 'd':
        shift = int(input('Enter the shift value for decryption: '))
        decrypted_text = caesar_decrypt(usr_str, shift)
        print(f'Decrypted text: {decrypted_text}\n')
    elif option == 'y':
        specific_word = input('Enter the word to count its occurrences: ')
        count = count_specific_word(usr_str, specific_word)
        print(f'The word "{specific_word}" appears {count} times.\n')


def word_frequency_counter(usr_str):
    # Counts the frequency of each word in the input string, ignoring punctuation.

    # Split the input string into individual words
    words = usr_str.split()
    word_freq = {}

    # Iterate through each word and count its frequency
    for word in words:
        # Remove common punctuation from the word and convert to lowercase for uniformity
        word = word.strip(".,!?").lower()

        # Check if the word is not empty
        if word:
            # Increment the count of the word if it exists in the frequency dictionary
            # Otherwise, initialize its count to 1
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

    return word_freq


def count_specific_word(usr_str, specific_word):
    # Counts the occurrences of a specific word in the input string, ignoring punctuation and case.

    # Split the input string into words
    words = usr_str.split()
    count = 0

    # Iterate through each word and count occurrences of the specific word
    for word in words:
        # Remove common punctuation from the word and convert to lowercase for uniformity
        word = word.strip(".,!?").lower()

        # Compare the word with the specific word, ignoring case
        if word == specific_word.lower():
            # Increment the count if the words match
            count += 1

    return count


def caesar_cipher(text, shift):
    # Encrypts the input text using the Caesar cipher technique with a specified shift.

    encrypted_text = ""
    # Apply Caesar cipher to each character in the text
    for char in text:
        if char.isupper():
            # Encrypt uppercase letters by shifting them based on the shift value
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            # Encrypt lowercase letters by shifting them based on the shift value
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Retain non-alphabetic characters as they are
            encrypted_text += char
    return encrypted_text


def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text


if __name__ == '__main__':
    menu_choice = ' '
    user_string = ''

    print('Enter text (press Enter twice to finish):')
    while True:
        line = input()
        if not line:
            break
        user_string += line + '\n'

    print(f'\nYou entered:\n{user_string}')
    print_menu()

    while menu_choice != 'q':
        menu_choice = input('Choose an option:\n')
        if menu_choice in ['c', 'w', 'f', 'r', 's', 'e', 'd', 'y']:
            execute_menu(menu_choice, user_string)
            print_menu()
