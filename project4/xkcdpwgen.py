#!/usr/bin/env python3
import argparse
import random
import string

# Define the word list
with open('cy2550/project4/words.txt', 'r') as f:
    word_list = [line.strip() for line in f]

def generate_password(num_words, num_caps, num_nums, num_symbols):
    # Select words randomly from the word list
    words = [random.choice(word_list) for _ in range(num_words)]
    # Capitalize random words
    checklist = list()
    for i in range(num_caps):
        capHelp(checklist, words)
    # Add random numbers
    nums = [str(random.randint(0, 9)) for _ in range(num_nums)]
    # Add random symbols
    symbols = [random.choice(string.punctuation) for _ in range(num_symbols)]
    # Concatenate the lists and shuffle
    password = words + nums + symbols
    random.shuffle(password)
    # Join the list into a string and return
    return ''.join(password)

def capHelp(checklist, words):
    index = random.randint(0, len(words) - 1)
    if index in checklist:
        capHelp(checklist, words)
    else:
        checklist.append(index)
        words[index] = words[index].capitalize()


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Generate a secure, memorable password using the XKCD method')
    parser.add_argument('-w', '--words', type=int, default=4, help='include WORDS words in the password (default=4)')
    parser.add_argument('-c', '--caps', type=int, default=0, help='capitalize the first letter of CAPS random words (default=0)')
    parser.add_argument('-n', '--numbers', type=int, default=0, help='insert NUMBERS random numbers in the password (default=0)')
    parser.add_argument('-s', '--symbols', type=int, default=0, help='insert SYMBOLS random symbols in the password (default=0)')
    args = parser.parse_args()

    # Generate and print the password
    password = generate_password(args.words, args.caps, args.numbers, args.symbols)
    print(password)

if __name__ == '__main__':
    main()
