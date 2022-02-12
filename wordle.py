#!/usr/bin/env python

import json

WORD_SIZE = 5
BLANK = '_'

spent_letters = []
misplaced_letters = {}
discovered_letters = [BLANK] * WORD_SIZE

with open("./wordle.json", 'r') as config_file:
    json_config = json.load(config_file)
    spent_letters = [c for c in json_config['spent_letters']]
    misplaced_letters = json_config['misplaced_letters']
    discovered_letters = [c for c in json_config['discovered_letters']]

best_guess = None
with open("./words.txt", 'r') as dictionary_file:
    possibility_count = 0
    for word in dictionary_file:
        word = word.strip()
        word_letters = set(word)
        invalid_word = False

        if len(word) != WORD_SIZE:
            continue

        for i in range(WORD_SIZE):
            required_letter = discovered_letters[i]
            if required_letter != BLANK:
                if word[i] != required_letter:
                    invalid_word = True
                    break;

        if invalid_word:
            continue

        for letter in misplaced_letters.keys():
            if not letter in word_letters:
                invalid_word = True
                break
            illegal_positions = misplaced_letters[letter]
            for position in illegal_positions:
                if word[position] == letter:
                    invalid_word = True
                    break

        for letter in spent_letters:
            if letter in word_letters:
                invalid_word = True
                break

        if not invalid_word:
            if None == best_guess:
                best_guess = word
            print(word)
            possibility_count += 1
    
    print("{count} possibilities".format(count = possibility_count))
    if None != best_guess:
        print("Best guess: {word}".format(word = best_guess))
