"""Checks which letters of the English alphabet are included in a given string. Nothing fancy."""

import argparse


def generate_alphabet():
    alphabet = []

    for i in range(97, 123):  # Range is [x, y)
        alphabet.append(chr(i))

    return alphabet

def determine_unique_letters_in_string(input_string):
    string_alphabet = []

    for char in input_string:
        if char.isalpha():
            if char not in string_alphabet:
                string_alphabet.append(char.lower())  # Normalize on lowercase
            else:
                pass

        else:  # If the current char isn't an alpha char, move on
            pass

    return string_alphabet

def compare_string_alphabet_to_english_alphabet(string_alphabet):
    english_alphabet_chars_unused = generate_alphabet()

    for char in string_alphabet:
        if char in english_alphabet_chars_unused:
            english_alphabet_chars_unused.remove(char)

    if english_alphabet_chars_unused == []:
        return "\n***Results***\nAll letters of the alphabet are present in the string!"

    else:
        return "\n***Results***\nThe following letters of the alphabet were NOT present in the string:\n%s" % \
                ", ".join(english_alphabet_chars_unused)

if __name__ == "__main__":
    # Setting up argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("input_string", help="String to the evaluated")
    args = parser.parse_args()

    # Parsing arguments
    input_string = args.input_string

    # Actual functionality
    string_alphabet = determine_unique_letters_in_string(input_string)
    results = compare_string_alphabet_to_english_alphabet(string_alphabet)

    print(results)
