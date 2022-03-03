import cmd
import os

import wget


# this wordlist is the list of all possible gueses that aren't solutions, as derived from the original game's javascript source
ALLOWED_GUESSES_URL = "https://gist.github.com/cfreshman/dec102adb5e60a8299857cbf78f6cf57/raw/15ec4eb961a969d6e263cea4d5b4a180bdeee7bd/allowed.txt"
# this wordlist is the list of all possible solutions, as derived from the original game's javascript source
ALLOWED_ANSWERS_URL = "https://gist.github.com/cfreshman/dec102adb5e60a8299857cbf78f6cf57/raw/15ec4eb961a969d6e263cea4d5b4a180bdeee7bd/answers.txt"
ALLOWED_GUESSES_FILENAME = "guesses.txt"
ALLOWED_ANSWERS_FILENAME = "answers.txt"


def read_word_list_file(filename):
    """
    Reads a text word list into a list of words, each of which have length word_length
    """
    with open(filename, 'r') as fh:
        return [line.strip() for line in fh]


def load_word_lists():
    """
    Returns the word lists of allowed guesses and allowed answers
    If word lists aren't present, download them.
    """
    if not os.path.exists(ALLOWED_GUESSES_FILENAME):
        wget.download(ALLOWED_GUESSES_URL, ALLOWED_GUESSES_FILENAME)
    if not os.path.exists(ALLOWED_ANSWERS_FILENAME):
        wget.download(ALLOWED_ANSWERS_URL, ALLOWED_ANSWERS_FILENAME)
    return read_word_list_file(ALLOWED_GUESSES_FILENAME), read_word_list_file(ALLOWED_ANSWERS_FILENAME)


def process_guess(word_list, guess, result):
    """
    Takes in the current list of possible words, a guess string, and a result string
    Returns the new list of possible words
    """
    assert len(guess) == 5, f"Word ({guess}) must have length 5"
    assert len(guess) == len(result), f'Result ({result}) must have the same length as word ({word})'
    for r in result:
        assert r in {'0', '1', '2'}, "Result characters must be 0, 1 or 2"
    to_remove = set()
    wrong_pos = set()
    right_pos = set()
    for position, (letter, result) in enumerate(zip(guess, result)):
        if result == '0':  # letter not in word at all
            to_remove.add(letter)
        elif result == '1':  # wrong position
            wrong_pos.add((letter, position))
        else:  # right position
            right_pos.add((letter, position))
    
    new_word_list = []
    for word in word_list:
        retain = True
        # first check if it's got a letter to be removed
        for c in to_remove:
            if c in word:
                retain = False
                break
        if not retain:
            continue
        # now check if it's got a letter in the right place
        for l, i in right_pos:
            if word[i] != l:
                retain = False
                break
        if not retain:
            continue
        # now check if it DOESN'T have a letter in the wrong place, but DOES have that letter
        for l, i in wrong_pos:
            if (word[i] == l) or (l not in word):
                retain = False
                break
        if not retain:
            continue
        new_word_list.append(word)
    return new_word_list


def generate_result(guess, solution):
    """ returns result string for guess if solution is the word being guessed"""
    solution_chars = frozenset(solution)
    return_string = ""
    for g, s in zip(guess, solution):
        if g == s:
            return_string += '2'
        elif g in solution_chars:
            return_string += '1'
        else:
            return_string += '0'
    return return_string


def suggest_guess(guesses, answers, num_suggestions=1):
    """
    Suggests guesses that minimize the number of possible solutions remaining
    """
    guess_sum = {}
    for guess in guesses + answers:
        guess_sum[guess] = 0
        for solution in answers:
            guess_sum[guess] += len(process_guess(answers, guess, generate_result(guess, solution)))
    ordered_guesses = [k for k in sorted(guess_sum, key=guess_sum.get)]
    return ordered_guesses[:num_suggestions]


class WordleShell(cmd.Cmd):
    intro = 'Welcome to a wordle assistant.   Type help or ? to list commands.\n'
    prompt = '(wordle-assist) '

    def __init__(self, guesses, answers):
        super(WordleShell, self).__init__()
        self.guesses = guesses
        self.answers = answers

    def do_show(self, arg):
        'Show all remaining possible words.'
        print(self.answers)

    def do_suggest(self, arg):
        'Suggest a number of words to guess. ex: SUGGEST 10'
        num_suggestions = 1
        if len(arg) > 0:
            num_suggestions = max(num_suggestions, int(arg))
        print(suggest_guess(guesses=self.guesses, answers=self.answers, num_suggestions=num_suggestions))

    def do_guess(self, arg):
        '''
        Process a guess and result: 
        0 for no match (grey)
        1 for right letter in the wrong place (yellow)
        2 for right letter in the right place (green)
        ex: GUESS unfit 00222
        '''
        arg_split = arg.split()
        word = arg_split[0].strip()
        result = arg_split[1].strip()
        old_num_answers = len(self.answers)
        self.answers = process_guess(self.answers, word, result)
        print(f'This guess reduced the set of possible solutions from {old_num_answers} candidates to {len(self.answers)}')
    
    def do_exit(self, arg):
        'Exit the wordle assistant'
        return True


if __name__ == '__main__':
    allowed_guesses, allowed_answers = load_word_lists()
    WordleShell(guesses=allowed_guesses, answers=allowed_answers).cmdloop()