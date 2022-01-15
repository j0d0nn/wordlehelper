#!/usr/bin/env python

import json

spent_letters = []
misplaced_letters = {}
discovered_letters = ['','','','','']

with open("./wordle.json", 'r') as config_file:
    json_config = json.load(config_file)
    spent_letters = json_config['spent_letters']
    misplaced_letters = json_config['misplaced_letters']
    discovered_letters = json_config['discovered_letters']

with open("./words.txt", 'r') as dictionary_file:
    possibility_count = 0
    for word in dictionary_file:
        word = word.strip().lower()
        word_letters = set(word)
        invalid_word = False

        if len(word) != 5:
            continue

        for i in range(5):
            required_letter = discovered_letters[i]
            if required_letter != '':
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
            print(word)
            possibility_count += 1
    
    print("{count} possibilities".format(count = possibility_count))
